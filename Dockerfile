# Base image
FROM python:3.9-slim-buster

COPY app/ /app

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Flask will be running on
EXPOSE 5000

# Set the entry point command
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
