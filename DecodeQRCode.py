import qrtools

qr = qrtools.QR()
qr.decode("left.png")
print qr.data