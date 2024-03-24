# import ubuntu image
FROM ubuntu:22.04

# set working directory
WORKDIR /app

# install dependencies
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# install reflex 
RUN pip install reflex