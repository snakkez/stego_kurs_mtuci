from helpers.exceptions import *
from algorithms.stegoalogrithm import StegoAlgorithm
from helpers.dct import DCT, IDCT
from file_io.bmpimage import BMPImage
from math import ceil, floor, copysign

class KochZhao(StegoAlgorithm):
    @staticmethod
    def calc_max_stego_data_size(img):
        return (((img.height // 8) * (img.width // 8) * 3) // 8)

    @staticmethod
    def construct_header(img, stego_size):
        pass

    @staticmethod
    def put_stego(img, stego_message):
        stego_data_len = len(stego_message)

        stego_message = bytearray('KZ', 'ascii')+stego_data_len.to_bytes(2, 'little') + stego_message

        stego_data_len += 4
        stego_img = BMPImage(img.export())

        if (stego_img.width*stego_img.height) < 704:
            raise ImageTooSmallException("Image is too small to contain header.")

        max_stego_size = KochZhao.calc_max_stego_data_size(stego_img)
        if stego_data_len > max_stego_size:
            raise StegomessageSizeException('Stegomessage is too long.')

        stego_img = KochZhao.put_stego_data(stego_img, stego_message)

        return stego_img

    @staticmethod
    def prepare_stego_data(stego_data):
        stego_data_conv = []
        for byte in stego_data:
            bin_byte = format(byte, '08b')
            stego_data_conv += [bin_byte[i:i+1] for i in range(0,8)]

        return stego_data_conv[::-1]

    @staticmethod
    def merge_bits(bits):
        bytes = [''.join(bits[i:i+8]) for i in range(0, len(bits),8)]
        if len(bytes[-1]) != 8:
            bytes.pop()

        return bytearray([int(byte, 2) for byte in bytes])

    @staticmethod
    def put_stego_data(img, stego_message):
        K1_c = (2, 6)
        K2_c = (3, 4)
        p_factor = 5
        stego_bits = KochZhao.prepare_stego_data(stego_message)
        dct_channels = DCT(img)
        for channel in dct_channels:
            for y in range(len(channel)):
                for x in range(len(channel[0])):
                    try:
                        cur_block = channel[y][x]
                        cur_bit = stego_bits.pop()
                        K1 = cur_block[K1_c[1]][K1_c[0]]
                        K2 = cur_block[K2_c[1]][K2_c[0]]
                        cur_coeff = abs(K1) - abs(K2)



                        if (cur_bit == '1') & (cur_coeff < p_factor):
                            K1, K2 = KochZhao.change_dist(K1, K2, p_factor)
                        if (cur_bit == '0') & (cur_coeff > -p_factor):
                            K1, K2 = KochZhao.change_dist(K1, K2, -p_factor)

                        cur_block[K1_c[1]][K1_c[0]] = K1
                        cur_block[K2_c[1]][K2_c[0]] = K2
                        channel[y][x] = cur_block

                    except IndexError:
                        return IDCT(dct_channels, img)
        return IDCT(dct_channels, img)
    @staticmethod
    def get_stego(stego_img):
        if (stego_img.width*stego_img.height) < 704:
            raise ImageTooSmallException("Image is too small to contain header.")

        stego_data_bits = KochZhao.get_stego_data(stego_img)

        stego_data_all = KochZhao.merge_bits(stego_data_bits)

        stego_header = stego_data_all[:4]

        if stego_header[:2] != bytearray('KZ', 'ascii'):
            raise NoHeaderFoundException('No header was found, aborting.')

        bytenum = int.from_bytes(stego_header[2:4], 'little')

        return stego_data_all[4:bytenum+4]



    @staticmethod
    def get_stego_data(stego_img):
        K1_c = (2, 6)
        K2_c = (3, 4)
        p_factor = 5
        stego_bits = []
        dct_channels = DCT(stego_img)
        for channel in dct_channels:
            for y in range(len(channel)):
                for x in range(len(channel[0])):
                    cur_block = channel[y][x]
                    K1 = cur_block[K1_c[1]][K1_c[0]]
                    K2 = cur_block[K2_c[1]][K2_c[0]]
                    cur_coeff = abs(K1) - abs(K2)
                    if cur_coeff < 0:
                        stego_bits.append('0')
                    else:
                        stego_bits.append('1')

        return stego_bits


    @staticmethod
    def change_dist(k1,k2,td):
        k1a, k2a = abs(k1), abs(k2)
        c_dis = k1a - k2a
        n_dis = c_dis - td

        a_dis = ceil(n_dis / 2) if n_dis > 0 else floor(n_dis / 2)


        k1a, k2a = k1a - a_dis, k2a + a_dis

        if k1a < 0:
            k2a += abs(k1a)
            k1a = 0
        if k2a < 0:
            k1a += abs(k2a)
            k2a = 0

        return k1a, k2a

