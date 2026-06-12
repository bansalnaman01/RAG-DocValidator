# 1. Start with the "OS" (Python 3.11)
FROM python:3.11-slim

# 2. Create a home for your project inside Docker
WORKDIR /app

# 3. Install Linux tools needed for FAISS and Math
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    libopenblas-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy your requirements list first (for faster building)
COPY requirements.txt .

# 5. Install all your libraries
RUN pip install --no-cache-dir -r requirements.txt

# 6. COPY ALL YOUR CODE (api.py, src folder, etc.)
COPY . .

# 7. Open the door for the Archer Dev (Port 8000)
EXPOSE 8000

# 8. Start the engine
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]