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


        KochZhao.put_stego_data(img, stego_message)

        return 0

    @staticmethod
    def prepare_stego_data(stego_data):
        stego_data_conv = []
        for byte in stego_data:
            bin_byte = format(byte, '08b')
            stego_data_conv += [bin_byte[i:i+1] for i in range(0,8)]

        return stego_data_conv[::-1]

    @staticmethod
    def put_stego_data(img, stego_message):
        K1_c = (2, 6)
        K2_c = (3, 4)
        p_factor = 5
        stego_bits = KochZhao.prepare_stego_data(stego_message)
        dct_channels = DCT(img)

        for channel in dct_channels:
            for y in range(len(dct_channels)):
                for x in range(len(channel)):
                    try:
                        cur_block = channel[y][x]
                        cur_bit = stego_bits.pop()
                        K1 = cur_block[K1_c[1]][K1_c[0]]
                        K2 = cur_block[K2_c[1]][K2_c[0]]
                        cur_coeff = abs(K1) - abs(K2)

                        if (cur_bit == '1') & (cur_coeff >= p_factor):
                            print(abs(K1) - abs(K2), cur_bit)
                        if (cur_bit == '1') & (cur_coeff < p_factor):
                            K1, K2 = KochZhao.change_dist(K1, K2, p_factor)
                            print('chng:', abs(K1) - abs(K2),  K1, K2, cur_bit)
                        if (cur_bit == '0') & (cur_coeff <= -p_factor):
                            print(abs(K1) - abs(K2), cur_bit)
                        if (cur_bit == '0') & (cur_coeff > -p_factor):
                            K1, K2 = KochZhao.change_dist(K1, K2, -p_factor)
                            print('chng:', abs(K1) - abs(K2), K1, K2, cur_bit)


                    except IndexError:
                        return IDCT(dct_channels, img)



    @staticmethod
    def change_dist(k1,k2,td):
        k1a, k2a = abs(k1), abs(k2)
        c_dis = k1a - k2a
        n_dis = c_dis + td
        add_dis = ceil(n_dis/2) if n_dis > 0 else floor(n_dis/2)
        print(add_dis)
        k1, k2 = k1-add_dis, k2+add_dis
        print(k1, k2)




    @staticmethod
    def get_stego():
        pass