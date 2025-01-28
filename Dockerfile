# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python file into the container
COPY app.py .

# Define the command to run the Python file
CMD ["python", "app.py"]