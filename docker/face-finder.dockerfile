FROM alpine:3.10.2

COPY ./requirements.txt /app/
COPY ./face_finder.py /app/
COPY ./resources/haarcascade_frontalface_default.xml /app/resources/

USER root
RUN apk add --update \
    python3 \
    py-pip 
    # build-base \
    # python-dev

USER $USER

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/face_finder.py"]
# CMD ["python", "face_finder.py"]
