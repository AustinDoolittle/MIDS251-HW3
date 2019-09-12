FROM nvcr.io/nvidia/l4t-base:r32.2.1

USER root

# configure timezone so tzdata doesn't prompt
# TODO hack, is there a way around this? why is tzdata necessary?
RUN echo "America/New_York" > etc/timezone
# Prevent prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libdc1394-22-dev \
    python-opencv \
    python3-opencv \
    python \
    python3 \
    python-pip \
    python3-pip

RUN pip3 install \
    numpy \
    paho-mqtt \
    protobuf

COPY face_finder.py /app/
COPY found_face_pb2.py /app/
COPY haarcascade_frontalface_default.xml /app/resources/

USER $USER

ENTRYPOINT [ "python3",  "/app/face_finder.py" ]
