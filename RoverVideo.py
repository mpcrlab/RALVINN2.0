from time import sleep
from rover import Rover20
from RoverControl import *
import cv2, numpy as np, pygame


class Rover(Rover20):
    def __init__(self):
        Rover20.__init__(self)
        pygame.init()
        self.file_name = 'filename'
        self.quit = False
        self.image = None
        self.run()
        self.rover = Rover20()

    def run(self):
        sleep(1.5)
        while not self.quit:
            self.process_video_from_rover()
        self.quit = True
        pygame.quit()

    def process_video_from_rover(self, jpegbytes, timestamp_10msec):
        try:
            window_name = 'Machine Perception and Cognitive Robotics'
            array_of_bytes = np.fromstring(jpegbytes, np.uint8)
            self.image = cv2.imdecode(array_of_bytes, flags=3)
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 440, 380)
            cv2.imshow(window_name, self.image)
            # waitkey cannot be zero
            cv2.waitKey(30)

        except:
            print("Could not find OpenCV")
