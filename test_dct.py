from algorithms.bmplsb import BMPLSB
from file_io.bmpimage import BMPImage
from helpers.dct import DCT, IDCT, VisualDCT


file = open('ts1.bmp', 'rb')
file_bytes = file.read()
file.close()
img = BMPImage(file_bytes)

chans = DCT(img)

vis = IDCT(chans, img)

file = open('ts2.bmp', "wb")
file.write(vis.export())
file.close

