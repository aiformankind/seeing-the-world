# Use an official tensorflow and latest stable release
FROM tensorflow/tensorflow

# Define environment variable
ENV IMAGE_SIZE=224
ENV ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"
ENV WORKPATH /seeing-the-world

# Set the working directory based on the WORKPATH
WORKDIR $WORKPATH

# Copy the current directory contents into the container based on the WORKPATH
COPY . $WORKPATH

# Make port 8888 and 6006 available to the world outside this container
EXPOSE 8888 6006

# Install any needed software and python packages
RUN apt-get update \
  && apt-get install -y \
     wget \
  && rm -rf /var/lib/apt/lists/* \
  && pip install Augmentor

# Run bash when the container launches
ENTRYPOINT ["/bin/bash"]