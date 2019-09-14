import argparse
import sys

from paho.mqtt import client


def parse_args(argv):
    parser = argparse.ArgumentParser('face-forwarder')
    parser.add_argument('--source-host', default='mqtt-arm')
    parser.add_argument('--dest-host', default='127.0.0.1')
    parser.add_argument('--topic', default='midsw251/hw3/+')
    parser.add_argument('--qos', type=int, default=1)
    return parser.parse_args(argv)


def main(args):
    # setup dest client
    dest_client = client.Client()
    dest_client.connect(args.source_host)

    # setup source client
    source_client = client.Client()

    def on_connect(client, userdata, flags, rc):
        source_client.subscribe(args.topic, qos=args.qos)

    source_client.on_connect = on_connect

    def on_message(client, userdata, msg):
        print(len(msg.payload))
        # dest_client.public(args.topic, payload=msg.payload)  
    
    source_client.on_message = on_message

    source_client.connect(args.source_host)
    source_client.loop_forever()

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)