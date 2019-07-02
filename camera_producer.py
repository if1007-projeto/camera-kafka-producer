import sys
import time
import threading

import cv2


class CameraProducer:

    def __init__(self, camera, kafka_producer, kafka_topic):
        self.camera = camera
        self.kafka_producer = kafka_producer
        self.kafka_topic = kafka_topic

    def __capture_frame_and_publish(self, camera):
        success, frame = camera.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        self.kafka_producer.send(self.kafka_topic, buffer.tobytes())

    def __start_producer(self, interval):
        """
        Publish camera video stream to specified Kafka topic.
        """

        frame_number = 1
        while self.camera.isOpened():
            try:
                self.__capture_frame_and_publish(self.camera)

                print('read %d frame(s)' % (frame_number))
                frame_number += 1

                time.sleep(interval)

            except:
                print("\nExiting.")
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
