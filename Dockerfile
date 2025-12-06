# Use official slim Python image
FROM python:3.12-slim

WORKDIR /bot

# Install only necessary system dependencies for sqlcipher3
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        sqlcipher \
        libsqlcipher-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements for caching
COPY requirements.txt .

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir sqlcipher3

# Copy project code
COPY . .

# Ensure Python outputs are unbuffered for Docker logs
ENV PYTHONUNBUFFERED=1

# Start bot
CMD ["python", "-u", "run.py"]
