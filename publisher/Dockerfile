# Use an official Ubuntu runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    pip3 install pyzmq

# Make port 5555 available to the world outside this container
EXPOSE 5555

# Run publisher.py when the container launches
CMD ["python3", "publisher.py"]
