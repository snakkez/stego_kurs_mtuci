from algorithms.bmplsb import BMPLSB
from file_io.bmpimage import BMPImage


file = open('ts1.bmp', 'rb')
file_bytes = file.read()
file.close()

img = BMPImage(file_bytes)

stego_msg = bytearray('aaaaaaaa'*200, 'ascii')

stego_img, params = BMPLSB.put_stego(img, stego_msg, depth=2, density=1)

print(params['density'])

opf = open('ts2.bmp', 'wb')
opf.write(stego_img.export())
opf.close()

a = input()

fil = open('ts2.bmp', 'rb')
fil_bytes = fil.read()
fil.close()

img2 = BMPImage(fil_bytes)

extracted_data = BMPLSB.get_stego(img2, 2)


print(stego_msg == extracted_data)

