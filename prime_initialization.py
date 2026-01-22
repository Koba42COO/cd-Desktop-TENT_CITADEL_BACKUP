import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import time
import math

# --- TENT v4.1 GEOMETRY ---
PHI = (1 + math.sqrt(5)) / 2
BASE_21_PRIMES = [1, 2, 4, 5, 7, 8, 10, 11, 13, 16, 17, 19, 20] # Solid resonances in Base 21 context (simplified)
# Note: In TENT, 3,6,9 are Flux. We avoid them for "Solid" crystallization.

def tent_prime_seed(shape):
    """
    Generates a weight matrix based on Prime Lattice Geometry.
    Instead of random noise, we use deterministic Prime harmonics derived from
    the matrix indices, scaled by Phi.
    
    Formula: W[i,j] = sin(Phi * (i^2 + j^2 + 1) * Prime[k]) * Scale
    """
    rows, cols = shape
    seed = torch.zeros(rows, cols)
    
    # Pre-compute prime lookups (cyclic)
    n_primes = len(BASE_21_PRIMES)
    
    for i in range(rows):
        for j in range(cols):
            # Geometric Address
            geo_hash = (i * cols + j)
            
            # Select Prime Harmonic based on address
            p = BASE_21_PRIMES[geo_hash % n_primes]
            
            # Phi-Resonance Function (Deterministically Chaotic but Bounded)
            # Using sin(Phi * ...) creates a low-discrepancy sequence distributed like a lattice
            val = math.sin(PHI * (geo_hash + 1) * p)
            
            # Scale adjustment (similar to Kaiming/Xavier to preserve variance)
            # Kaiming/He Init scaling: sqrt(2 / fan_in)
            fan_in = cols
            scale = math.sqrt(2.0 / fan_in)
            
            seed[i, j] = val * scale

    return seed

class TentPrimeLinear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        
        # Initialize weights with TENT Geometry
        self.weight = nn.Parameter(tent_prime_seed((out_features, in_features)))
        # Bias initialized to zero (standard) or small prime harmonic? Let's stick to 0 for controlled variable.
        self.bias = nn.Parameter(torch.zeros(out_features))

    def forward(self, input):
        return nn.functional.linear(input, self.weight, self.bias)

# --- MODELS ---    
class StandardNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        
        # Standard Kaiming/He Initialization (Default Gaussian/Uniform usually, ensuring Kaiming here)
        nn.init.kaiming_normal_(self.fc1.weight, mode='fan_in', nonlinearity='relu')
        nn.init.xavier_normal_(self.fc2.weight)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

class PrimeNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        # Use TENT Initialized Layers
        self.fc1 = TentPrimeLinear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = TentPrimeLinear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# --- EXPERIMENT ---
def run_experiment():
    print("--- 💎 THE CRYSTAL SEED EXPERIMENT (PHASE 217) 💎 ---")
    print("Hypothesis: Prime-Seeded Initialization converges faster than Random Gaussian.")
    
    # 1. Synthetic Dataset (Generalization Test)
    # Target: y = sin(x) + cos(phi * x) (Non-linear, periodic)
    # This tests the network's ability to find harmonic structure.
    N_SAMPLES = 2000
    INPUT_DIM = 20
    HIDDEN_DIM = 128
    OUTPUT_DIM = 1
    
    # Generate data lying on a manifold (not random noise)
    torch.manual_seed(42) # Fixed data seed
    X = torch.randn(N_SAMPLES, INPUT_DIM)
    # The true function uses specific indices to simulate structure
    true_weights = torch.tensor([math.sin(i * PHI) for i in range(INPUT_DIM)]).unsqueeze(1)
    Y = torch.matmul(X, true_weights) + 0.1 * torch.randn(N_SAMPLES, 1) # Add slight noise
    Y = torch.sin(Y) # Non-linear activation

    # Split Train/Test
    split = int(0.8 * N_SAMPLES)
    X_train, X_test = X[:split], X[split:]
    Y_train, Y_test = Y[:split], Y[split:]
    
    train_dataset = torch.utils.data.TensorDataset(X_train, Y_train)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
    
    # 2. Setup Models
    std_model = StandardNet(INPUT_DIM, HIDDEN_DIM, OUTPUT_DIM)
    prime_model = PrimeNet(INPUT_DIM, HIDDEN_DIM, OUTPUT_DIM)
    
    models = [("Standard (Gaussian)", std_model), ("TENT (Prime Seed)", prime_model)]
    results = {}
    
    criterion = nn.MSELoss()
    EPOCHS = 20
    
    # 3. Train Loop
    for name, model in models:
        print(f"\nTraining {name}...")
        optimizer = optim.Adam(model.parameters(), lr=0.005)
        loss_history = []
        test_history = []
        
        start_time = time.time()
        
        for epoch in range(EPOCHS):
            model.train()
            epoch_loss = 0
            for batch_X, batch_Y in train_loader:
                optimizer.zero_grad()
                pred = model(batch_X)
                loss = criterion(pred, batch_Y)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
            
            avg_loss = epoch_loss / len(train_loader)
            loss_history.append(avg_loss)
            
            # Test
            model.eval()
            with torch.no_grad():
                test_pred = model(X_test)
                test_loss = criterion(test_pred, Y_test).item()
                test_history.append(test_loss)
                
            if epoch % 5 == 0:
                print(f"  Epoch {epoch}: Train Loss {avg_loss:.5f} | Test Loss {test_loss:.5f}")
                
        duration = time.time() - start_time
        results[name] = {
            "final_train_loss": loss_history[-1],
            "final_test_loss": test_history[-1],
            "duration": duration,
            "convergence_epoch": np.argmax(np.array(test_history) < 0.1) if min(test_history) < 0.1 else "N/A"
        }
        
    # 4. Report
    print("\n--- 📊 RESULTS SUMMARY ---")
    print(f"{'Model':<25} | {'Test Loss':<10} | {'Time (s)':<10} | {'Improvement'}")
    print("-" * 65)
    
    base_loss = results["Standard (Gaussian)"]["final_test_loss"]
    tent_loss = results["TENT (Prime Seed)"]["final_test_loss"]
    improvement = ((base_loss - tent_loss) / base_loss) * 100
    
    for name, metrics in results.items():
        print(f"{name:<25} | {metrics['final_test_loss']:.5f}    | {metrics['duration']:.2f}s      |")
        
    print("-" * 65)
    print(f"TENT Efficiency Delta: {improvement:+.2f}% lower error rate (Generalization)")
    
    if improvement > 0:
        print("VERDICT: CANDIDATE CRYSTALLIZED. TENT Geometry outperforms Entropy.")
    else:
        print("VERDICT: NO SIGNIFICANT GAIN. Chaos prevails.")

if __name__ == "__main__":
    try:
        run_experiment()
    except ImportError:
        print("Error: PyTorch not installed. Please run `pip install torch` first.")
    except Exception as e:
        print(f"An error occurred: {e}")
