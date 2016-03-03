import pyqrcode

# Run this code to create your own QR code.

######################################
qr = pyqrcode.create("TURN LEFT")
# Add your command to .create()
qr.png('left.png', scale=6)
# QR code is created, you can rename it to whatever you want.
######################################
