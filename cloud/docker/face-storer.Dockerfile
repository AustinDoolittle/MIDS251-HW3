FROM nvcr.io/nvidia/l4t-base:r32.2.1

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
COPY face_storer.py /app/
COPY found_face_pb2.py /app/

ENTRYPOINT [ "python3", "/app/face_storer.py" ]