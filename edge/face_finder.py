import logging
import sys
import argparse

import numpy as np
import cv2
from paho.mqtt import client

DEFAULT_MODEL_FILE = '/app/resources/haarcascade_frontalface_default.xml'

logger = logging.getLogger('face-finder')
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def parse_args(argv):
    parser = argparse.ArgumentParser('face-finder')
    parser.add_argument('--model-file', default=DEFAULT_MODEL_FILE)
    parser.add_argument('--mqtt-host', default='mqtt')
    parser.add_argument('--headless', action='store_true')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args(argv)

def main(args):
    log_level = logging.DEBUG if args.debug else logging.INFO
    logger.setLevel(log_level)

    # Initialize our necessary stuff
    logger.info('Initializing video capture...')
    cap = cv2.VideoCapture(0)

    logger.info('Initializing classifier...')
    face_cascade = cv2.CascadeClassifier(args.model_file)

    logger.info(f'Initializing and connecting to mosquitto broker at "{args.mqtt_host}"')
    mqtt_client = client.Client()
    mqtt_client.connect(args.mqtt_host)

    while True:
        # grab an image and detect the face
        ret, frame = cap.read()

        if not ret:
            logger.info('Failed to grab frame.')
            continue
        
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grey_frame, 1.3, 5)

        for i, (x,y,w,h) in enumerate(faces):
            logger.debug(f'Face{i}: x: {x}, y: {y}, w: {w}, h: {h}')
            if not args.headless:
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv2.rectangle(
                    grey_frame, 
                    top_left, 
                    bottom_right, 
                    color=255,
                    thickness=10
                )

        if not args.headless:
            cv2.imshow("faces!", grey_frame)
            cv2.waitKey(1)



if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
