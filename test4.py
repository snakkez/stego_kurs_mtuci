from algorithms.kochzhao import KochZhao
from file_io.bmpimage import BMPImage
from random import choice
from string import ascii_letters




file = open('ts3.bmp', 'rb')
file_bytes = file.read()
file.close()


img = BMPImage(file_bytes)
rand_msg = ''.join([choice(ascii_letters) for i in range(100)])
print(rand_msg)
stego_msg = bytearray(rand_msg, 'ascii')
stego_img = KochZhao.put_stego(img, stego_msg)

opf = open('ts2.bmp', 'wb')
opf.write(stego_img.export())
opf.close()


fil = open('ts2.bmp', 'rb')
fil_bytes = fil.read()
fil.close()

img2 = BMPImage(fil_bytes)

extracted_data = KochZhao.get_stego(img2)

print(stego_msg == extracted_data)
print(stego_msg)
print(extracted_data)
