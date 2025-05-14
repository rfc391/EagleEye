FROM python:3.13.2-slim

# Set environment
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /opt/eagleeye

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY src/ ./src/
COPY config/ ./config/
COPY scripts/ ./scripts/

# Run the CLI by default
ENTRYPOINT ["python3", "src/cli.py"]