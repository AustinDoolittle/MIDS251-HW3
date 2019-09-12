FROM alpine:3.10.2

USER root

RUN apk add \
    python \
    python3 \
    py-pip \
    py3-pip

RUN pip3 install paho-mqtt 

COPY face_forwarder.py /app/
COPY found_face_pb2.py /app/

ENTRYPOINT [ "python3", "/app/face_forwarder.py" ]
