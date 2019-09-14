import argparse
import sys

from paho.mqtt import client

from util import get_logger

logger = get_logger(__name__)


def parse_args(argv):
    parser = argparse.ArgumentParser('face-forwarder')
    parser.add_argument('--source-host', default='mqtt-arm')
    parser.add_argument('--dest-host', default='127.0.0.1')
    parser.add_argument('--topic', default='midsw251/hw3/+')
    parser.add_argument('--qos', type=int, default=1)
    return parser.parse_args(argv)


def main(args):
    logger.info('Starting up face forwarder...')

    # setup dest client
    logger.info('Creating destination client...')
    dest_client = client.Client()
    dest_client.connect(args.source_host)
    dest_client.loop_start()

    # setup source client
    logger.info('Creating source client')
    source_client = client.Client()

    def source_on_connect(client, userdata, flags, rc):
        logger.info('Source client connected successfully')
        source_client.subscribe(args.topic, qos=args.qos)


    source_client.on_connect = source_on_connect

    def source_on_message(client, userdata, msg):
        logger.info(f'Forwarding {len(msg.payload)} byte message')
        dest_client.publish(args.topic, payload=msg.payload, qos=1)  
    
    source_client.on_message = source_on_message

    logger.info('Connecting to source client')
    source_client.connect(args.source_host)
    source_client.loop_forever()

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)