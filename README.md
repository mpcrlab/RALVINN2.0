#                                 Rover Autonomous Land Vehicle in a Neural Network
-------------------------------------------------------

                        Machine Perception and Cognitive Robotics Laboratory
                            Center for Complex Systems and Brain Sciences
                                    Florida Atlantic University
-------------------------------------------------------
##Info

        This is the second version of the RALVINN code. It uses OpenCV to read the images from
        the BrookStone Rover instead of PyGame. 

##Current Status

        This is a work in progress by the members of the FAU Machine Perception Club. You may 
        encounter bugs and other issues when running this code. 

##Getting Started with RALVINN.

        Before running the code you will need to make sure that the following python packages 
        have been installed

        1)OpenCV 3.0
        2)PyPNG
        3)PyQrCode and QRTools
        4)PyGame
        5)cStringIO

##How to connect to BrookStone Rover.

        1)Open your WIFI settings. 
        2)Finds the Rover SSID, it usually starts with Rover_ROVERID.
        3)Connect the SSID ID. The green LED light on the Rover will stop flashing once 
        a connection has been established.


##How to create a QR Code.
        To create a QR code you will need to run CreateQRCode. This python script creates a qr code with 
        whatever command you give it.
        
##How does the BrookStone Rover Read QR Codes?
        Withing the RoverPylot script there is method called refresh_video_feed. That scripts saves 
        the image array into a file named "qr.ong". Then when the rover sees the QR in the feed the 
        function qr_tools uses the built in function decoder to decode the meaning of the QR code.
##Getting started with the BrookStone Rover 2.0.
        Run MPCR_RALVINN.py. If everything has been installed correctly a window will pop up showing the
        Rover video feed. Use the keyboard commands below to move the BrookStone Rover 2.0

##How to control the BrookStone Rover 2.0:
        W - Forward
        S - Back
        D - Right
        A - LEFT
        U - Toggle Infrared Night Vision.
        J - Camera Up
        K - Camera Down
        I - Toggle Lights
        Space bar - Take a pic.
        
##To Do List
     1)Give the BrookStone Rover 2.0 the ability to read QR codes.
      2)Apply Reinforcement Learning using the QR codes to create positive and negative feedback.  
      3)Add more helper functions.
      4)Fix Bugs!
          * Corrupt JPEG DATA - Only seen on Linux system. Will need to investigate. Does not affect Rover.
        