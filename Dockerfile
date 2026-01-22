# TENT Citadel v5.0 - Sovereign AI Stack
FROM python:3.11-slim

LABEL maintainer="Bradley Wallace <koba42coo>"
LABEL description="TENT Citadel - Sovereign AI with Constitutional Governance"

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create model and data directories
RUN mkdir -p /app/citadel/models /app/citadel/library /app/citadel/ingest /app/hippocampus

# Expose Streamlit port
EXPOSE 8501

# Environment
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_HEADLESS=true

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Default command - run Streamlit Command Center
CMD ["streamlit", "run", "tent_app.py", "--server.address=0.0.0.0"]
