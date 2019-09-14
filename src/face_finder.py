import sys
import argparse
import uuid

import numpy as np
import cv2
from paho.mqtt import client

from found_face_pb2 import FoundFace
from util import get_logger


logger = get_logger(__name__)


DEFAULT_MODEL_FILE = '/app/resources/haarcascade_frontalface_default.xml'


def parse_args(argv):
    parser = argparse.ArgumentParser('face-finder')
    parser.add_argument('--model-file', default=DEFAULT_MODEL_FILE)
    parser.add_argument('--mqtt-host', default='mqtt-arm')
    parser.add_argument('--headless', action='store_true')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--topic-prefix', default='midsw251/hw3/')
    return parser.parse_args(argv)


def get_uuid():
    return str(uuid.uuid1())


def crop_image(img, x, y, w, h):
    return img[y:y+h, x:x+w]


def overlay_rectangle(img, x, y, w, h):
    top_left = (x, y)
    bottom_right = (x + w, y + h)
    cv2.rectangle(
        img, 
        top_left, 
        bottom_right, 
        color=255,
        thickness=10
    )


def compile_message(img, x, y, w, h):
    ff = FoundFace()
    ff.image_id = get_uuid()
    ff.image_data = cv2.imencode('.jpg', img)[1].tostring()
    ff.bbox.x = x
    ff.bbox.y = y
    ff.bbox.w = w
    ff.bbox.h = h

    return ff.SerializeToString()

def main(args):
    # Initialize our necessary stuff
    logger.info('Initializing video capture...')
    cap = cv2.VideoCapture(0)

    logger.info('Initializing classifier...')
    face_cascade = cv2.CascadeClassifier(args.model_file)

    logger.info(f'Initializing and connecting to mosquitto broker at "{args.mqtt_host}"')
    mqtt_client = client.Client()
    mqtt_client.connect(args.mqtt_host)
    mqtt_client.loop_start()

    host_id = get_uuid()
    topic = args.topic_prefix + host_id
    logger.info(f'Publishing to topic "{topic}""')

    while True:
        # grab an image and detect the face
        ret, frame = cap.read()

        if not ret:
            logger.info('Failed to grab frame.')
            continue
        
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grey_frame, 1.3, 5)

        for x, y, w, h in faces:
            # crop the face 
            cropped_image = crop_image(grey_frame, x, y, w, h)

            # construct message
            compiled_message = compile_message(
                cropped_image, 
                x, y, w, h
            )

            # publish it to the queue
            mqtt_client.publish(topic, payload=compiled_message, qos=1)

            if not args.headless:
                overlay_rectangle(grey_frame, x, y, w, h)


        if not args.headless:
            cv2.imshow("faces!", grey_frame)
            cv2.waitKey(1)



if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
