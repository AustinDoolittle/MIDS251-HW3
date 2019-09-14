FROM nvcr.io/nvidia/l4t-base:r32.2.1

USER root

# install dependencies
RUN apt-get update && \
    apt install -y  \
        libtbb-dev \
        libavcodec-dev \
        libavformat-dev \
        libgstreamer1.0-dev \
        libgstreamer-plugins-base1.0-dev \
        libgtk2.0-dev \
        libswscale-dev \
        libv4l-dev \
        python \
        python3 \
        python-pip \
        python3-pip \
        curl

# download opencv debs
ARG URL=http://169.44.201.108:7002/jetpacks/4.2.1

RUN curl $URL/libopencv_3.3.1-2-g31ccdfe11_arm64.deb  -so /tmp/libopencv_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb -so /tmp/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb -so /tmp/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb

# install and clean up
RUN dpkg -i /tmp/*.deb
RUN rm -rf /tmp/*

# install python packages
RUN pip3 install \
    numpy \
    paho-mqtt \
    protobuf

# copy source files
COPY src/face_finder.py /app/
COPY src/util.py /app/
COPY src/found_face_pb2.py /app/
COPY resources/haarcascade_frontalface_default.xml /app/resources/

ENTRYPOINT [ "python3",  "/app/face_finder.py" ]
