# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY . /app

RUN pip3 install -r requirements.txt
# Expose the port that the Flask app will run on
EXPOSE 5000

# Run the Flask app when the container starts
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]