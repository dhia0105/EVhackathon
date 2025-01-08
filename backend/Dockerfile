# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies for SQL connection and other tools
RUN apt-get update && \
    apt-get install -y gcc python3-dev libsasl2-dev libldap2-dev libssl-dev && \
    apt-get clean

# Install required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
