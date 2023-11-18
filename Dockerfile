# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Expose the port that Django runs on
EXPOSE 8000

# Define the command to run your Django project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]