from algorithms.bmplsb import BMPLSB
from file_io.bmpimage import BMPImage
from errors.errors import *
from random import choice
from string import ascii_letters




file = open('ts1.bmp', 'rb')
file_bytes = file.read()
file.close()
img = BMPImage(file_bytes)

rand_msg = ''.join([choice(ascii_letters) for i in range(360000)])
stego_msg = bytearray(rand_msg, 'cp1251')
stego_img = BMPLSB.put_stego(img, stego_msg, depth=4, density=1)


mse = calculate_MSE(img, stego_img)
psnr = calculate_PSNR(img, stego_img, mse)
nmse = calculate_NMSE(img, stego_img, mse)
snr = calculate_SNR(img, stego_img)
print(mse, nmse, snr, psnr)

opf = open('ts2.bmp', 'wb')
opf.write(stego_img.export())
opf.close()


fil = open('ts2.bmp', 'rb')
fil_bytes = fil.read()
fil.close()

img2 = BMPImage(fil_bytes)

extracted_data = BMPLSB.get_stego(img2, 4, 1)

print(stego_msg == extracted_data)
