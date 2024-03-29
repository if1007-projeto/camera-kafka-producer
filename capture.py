#!/usr/bin/env python3

import time
import argparse
import cv2
import traceback
import logging

from kafka import KafkaProducer
from camera_producer import CameraProducer

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('CameraProducer')

connection_retries = 1000


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


def try_connect_kafka():
    for attempt in range(connection_retries):
        logger.debug('attempt to connect to kafka - %d tries' % (attempt))
        try:
            producer = KafkaProducer(bootstrap_servers=kafka_url)

            return producer

        except:
            logger.error('error connecting')
            traceback.print_exc()
            
        time.sleep(1)


args = get_command_line_arguments()

urls_comma_separated = args.camera_urls
kafka_topic = args.kafka_topic
kafka_url = args.kafka_url
camera_urls = urls_comma_separated.split(',')

logger.info('kafka -- url: %s, topic: %s' % (kafka_url, kafka_topic))

producer = try_connect_kafka()

async_mode = len(camera_urls) > 1

for camera_url in camera_urls:
    logger.info('start \"%s\" source input' % (camera_url))

    try:
        camera = cv2.VideoCapture(camera_url)
        camera_producer = CameraProducer(
            camera=camera,
            kafka_producer=producer,
            kafka_topic=kafka_topic)
        camera_producer.start(interval=0.0001, async_mode=async_mode)

    except:
        traceback.print_exc()
