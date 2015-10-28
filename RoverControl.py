from pygame.locals import *
from rover import Rover20
import pygame,sys


class Steer:
    def __init__(self):
        self.rover_object = Rover20()
        pygame.init()
        self.window = pygame.display.set_mode((800,600))
        self.caption = pygame.display.set_caption("Window")
        self.rover_run = True
        self.steer()

    def steer(self):

        while self.rover_run:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    keyboard_input = pygame.key.get_pressed()

                    if keyboard_input[K_w]:
                        print("Forward")
                        self.rover_object.set_wheel_treads(1, 1)
                    elif keyboard_input[K_s]:
                        print("Backwards")
                        self.rover_object.set_wheel_treads(-1, -1)
                    elif keyboard_input[K_a]:
                        print("Left")
                        self.rover_object.set_wheel_treads(-1, 1)
                    elif keyboard_input[K_d]:
                        print("Right")
                        self.rover_object.set_wheel_treads(1, -1)
                    elif keyboard_input[K_q]:
                        print("Left")
                        self.rover_object.set_wheel_treads(.1, 1)
                    elif keyboard_input[K_e]:
                        print("Right")
                        self.rover_object.set_wheel_treads(1, .1)
                    elif keyboard_input[K_z]:
                        print("Reverse Left")
                        self.rover_object.set_wheel_treads(-.1, -1)
                    elif keyboard_input[K_c]:
                        print("Reverse Right")
                        self.rover_object.set_wheel_treads(-1, -.1)
                    elif keyboard_input[K_q]:
                        print("Left")
                        self.rover_object.set_wheel_treads(.1, 1)
                    elif keyboard_input[K_j]:
                        print("Camera Up")
                        self.rover_object.move_camera_in_vertical_direction(1)
                    elif keyboard_input[K_k]:
                        print("Camera Down")
                        self.rover_object.move_camera_in_vertical_direction(-1)
                    elif keyboard_input[K_u]:
                        print("Lights On")
                        self.rover_object.turn_the_lights_on()
                    elif keyboard_input[K_i]:
                        print("Lights On")
                        self.rover_object.turn_the_lights_off()












                    elif keyboard_input[K_ESCAPE]:
                        self.rover_run = False
                        pygame.display.quit()
                        pygame.quit()
                elif event.type == KEYUP:
                    self.rover_object.set_wheel_treads(0, 0)


if __name__ == '__main__':
    Steer()
