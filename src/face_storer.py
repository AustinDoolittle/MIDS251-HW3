import argparse
import sys
import io
import logging

from paho.mqtt import client as mqtt
import ibm_boto3

from found_face_pb2 import FoundFace
from util import get_logger

logger = get_logger(__name__)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', default='face-bucket')
    parser.add_argument('--mqtt-host', default='mqtt')
    parser.add_argument('--topic', default='midsw251/hw3/+')

    return parser.parse_args(argv)


def main(args):
    logger.info('Creating object store client')
    cos_client = ibm_boto3.client("s3")

    logger.info('Creating mosquitto client')
    mqtt_client = mqtt.Client()

    # setup source client
    def on_connect(client, userdata, flags, rc):
        logger.info('Mosquitto client connected successfully')
        mqtt_client.subscribe(args.topic, qos=1)

    mqtt_client.on_connect = on_connect

    def on_message(client, userdata, msg):
        try:
            logger.info(f'{len(msg.payload)} byte message recieved')
            ff = FoundFace.ParseFromString(msg.payload)
            buf = io.BytesIO(ff.image_data) 

            logger.info(f'Uploading to {args.bucket}/{ff.image_id}')
            cos_client.upload_fileobj(buf, args.bucket, ff.image_id)
        except Exception as e:
            logger.error(str(e))

    
    mqtt_client.on_message = on_message

    logger.info('Connecting to mosquitto broker')
    mqtt_client.connect(args.mqtt_host)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)