import torch, torch.nn as nn, hashlib
class TentPrimeLinear(nn.Module):
    def __init__(self, i, o):
        super().__init__()
        self.weight, self.bias = nn.Parameter(torch.randn(o,i)*0.1), nn.Parameter(torch.zeros(o))
    def forward(self, x): return x @ self.weight.T + self.bias
class SovereignBrain(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1, self.l2 = TentPrimeLinear(64,32), TentPrimeLinear(32,1)
    def forward(self, x): return torch.sigmoid(self.l2(torch.tanh(self.l1(x))))
    def vectorize(self, t):
        h = hashlib.sha256(t.encode()).hexdigest()
        return torch.tensor([int(h[i:i+2],16)/255 for i in range(0,128,2)]).unsqueeze(0)
