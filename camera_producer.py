import sys
import time
import threading

import cv2
import struct
import traceback

import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')


class CameraProducer:

    def __init__(self, camera, kafka_producer, kafka_topic):
        self.camera = camera
        self.kafka_producer = kafka_producer
        self.kafka_topic = kafka_topic
        self.logger = logging.getLogger('CameraProducer')

    def __capture_frame_and_publish(self, camera):
        success, frame = camera.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        self.kafka_producer.send(self.kafka_topic, buffer.tobytes())

    def __start_producer(self, interval):
        """
        Publish camera video stream to specified Kafka topic.
        """

        frame_number = 1
        start_time = time.time()
        while self.camera.isOpened():
            try:
                self.__capture_frame_and_publish(self.camera)

                frame_number += 1

                elapsed_time = time.time() - start_time
                if elapsed_time > 1: 
                    start_time = time.time()
                    self.logger.debug('read %d frame(s)' % (frame_number))

                time.sleep(interval)

            except:

                traceback.print_exc()

                self.logger.error("\nExiting.")
                sys.exit(1)

        self.camera.release()

    def start(self, async_mode=False, interval=0.2):
        if async_mode == True:
            self.thread = threading.Thread(
                target=self.__start_producer, args=(interval,))
            self.thread.start()
        else:
            self.__start_producer(interval)

    def stop(self):
        self.thread.stop()
