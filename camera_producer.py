import sys
import time
import threading

from kafka import KafkaProducer
import cv2


class CameraProducer:

    def __init__(self, camera_url, kafka_url, kafka_topic):
        self.camera_url = camera_url    
        self.kafka_url = kafka_url
        self.kafka_topic = kafka_topic

        def __capture_frame_and_publish(self, camera, producer):
            success, frame = camera.read()
            ret, buffer = cv2.imencode('.jpg', frame)
            producer.send(self.kafka_topic, buffer.tobytes())

    def __start_producer(self, interval):
        """
        Publish camera video stream to specified Kafka topic.
        """
        camera = cv2.VideoCapture(self.camera_url)
        producer = KafkaProducer(bootstrap_servers=self.kafka_url)

        frame_number = 1
        while camera.isOpened():
            try:
                self.__capture_frame_and_publish(camera, producer)

                print('read %d frame(s)' % (frame_number))
                frame_number += 1

                time.sleep(interval)

            except:
                print("\nExiting.")
                sys.exit(1)

        camera.release()

    def start(self, async_mode=False, interval=0.2):
        if async_mode == True:
            self.thread = threading.Thread(target=self.__start_producer, args=(interval,))
            self.thread.start()
        else:
            self.__start_producer(interval)

    def stop(self):
        self.thread.stop()