from rover import Rover20
from pygame.locals import *
import numpy as np
import pygame
import cv2


class Ralvinn(Rover20):
    def __init__(self):
        """



        """
        Rover20.__init__(self)
        self.file_name = 'filename'
        pygame.init()


    def process_video_from_rover(self, jpegbytes, timestamp_10msec):
        try:
            window_name = 'Rover'
            array_of_bytes = np.fromstring(jpegbytes, np.uint8)
            img_np = cv2.imdecode(array_of_bytes, flags=3)
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(window_name, 440, 380)
            cv2.imshow(window_name, img_np)
            cv2.waitKey(5)
        except:
            print("Could not find OpenCV")

    def steer_rover(self):
        pass

        # for event in pygame.event.get():
        #     if event.type == KEYDOWN:
        #         key_pressed = pygame.key.get_pressed()
        #
        #         if key_pressed[pygame.K_w]:
        #             print("Forward")
        #     elif event.type ==pygame.KEYUP:
        #         self.set_wheel_treads(0,0)