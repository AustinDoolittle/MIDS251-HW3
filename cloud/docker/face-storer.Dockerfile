FROM nvcr.io/nvidia/l4t-base:r32.2.1

# install dependencies
RUN apt-get update && \
    apt-get install -f \
        python \
        python3 \
        python-pip \
        python3-pip

# install required python packages
RUN pip3 install -y \
    paho-mqtt \
    ibm-cos-sdk

# copy source
COPY face_storer.py /app/

ENTRYPOINT [ "python", "/app/face_storer.py" ]