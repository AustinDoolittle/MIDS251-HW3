FROM ubuntu:18.04

# install dependencies
RUN apt-get update && \
    apt-get install -y \
        python \
        python3 \
        python-pip \
        python3-pip

# install required python packages
RUN pip3 install \
    paho-mqtt \
    ibm-cos-sdk \
    protobuf

# copy source
COPY src/face_storer.py /app/
COPY src/util.py /app/
COPY src/found_face_pb2.py /app/

ENV HOME /app/

ENTRYPOINT [ "python3", "/app/face_storer.py" ]