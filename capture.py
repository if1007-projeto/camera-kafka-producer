#!/usr/bin/env python3

import argparse
from camera_producer import CameraProducer

def get_command_line_arguments():
    parser = argparse.ArgumentParser(
        description='Send camera stream to kafka. ')
    parser.add_argument('-s', '--video-source', dest='camera_urls', metavar='<url>,<url>,...,<url>', required=True, type=str,
                        help='a commad-separated list of camera urls. Example: http://192.168.100.10/stream,http://192.168.100.12/stream')

    parser.add_argument('-d', '--kafka-url', dest='kafka_url', metavar='<destination>', required=True, type=str,
                        help='kafka url to publish frames')

    parser.add_argument('-t', '--kafka-topic', dest='kafka_topic', metavar='<kafka topic>', required=True, type=str,
                        help='kafka topic to publish frames')

    args = parser.parse_args()

    return args


args = get_command_line_arguments()

urls_comma_separated = args.camera_urls
kafka_topic = args.kafka_topic
kafka_url = args.kafka_url
camera_urls = urls_comma_separated.split(',')

for camera_url in camera_urls:
    print('start \"%s\" source input' % (camera_url))
    camera_producer = CameraProducer(camera_url=camera_url, kafka_url=kafka_url, kafka_topic=kafka_topic)
    camera_producer.start(interval=0.0001, async_mode=True)
