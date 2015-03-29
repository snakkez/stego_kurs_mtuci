from algorithms.bmplsbinterval import BMPLSBInterval
from file_io.bmpimage import BMPImage
from random import choice
from string import ascii_letters




file = open('ts1.bmp', 'rb')
file_bytes = file.read()
file.close()
img = BMPImage(file_bytes)
rand_msg = ''.join([choice(ascii_letters) for i in range(10000)])
print(rand_msg)
stego_msg = bytearray(rand_msg, 'ascii')
stego_img = BMPLSBInterval.put_stego(img, stego_msg, 300, 32, depth=4)


opf = open('ts2.bmp', 'wb')
opf.write(stego_img.export())
opf.close()


fil = open('ts2.bmp', 'rb')
fil_bytes = fil.read()
fil.close()

img2 = BMPImage(fil_bytes)

extracted_data = BMPLSBInterval.get_stego(img2, 300,32,depth=4)

print(stego_msg == extracted_data)
print(stego_msg)
print(extracted_data)