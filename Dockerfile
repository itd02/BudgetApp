# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for OpenGL and other packages
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app and images into the container
COPY . .

# Expose the port that Flask runs on
EXPOSE 5001

# Command to run the Flask app
CMD ["python", "main.py"]
