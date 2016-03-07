import pyqrcode

# Run this code to create your own QR code.

######################################
qr = pyqrcode.create("TURN RIGHT")
# Add your command to .create()
qr.png('turnright.png', scale=6)
# QR code is created, you can rename it to whatever you want.
######################################
