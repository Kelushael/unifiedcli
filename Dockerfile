FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Install package
RUN pip install -e .

# Create data directory
RUN mkdir -p /app/data

# Expose MCP port
EXPOSE 8000

# Default to shell
CMD ["unified-cli", "shell"]
