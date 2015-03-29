from .bmplsb import BMPLSB
from helpers.exceptions import *
import random

class DistributionCeilException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)

class BMPLSBInterval(BMPLSB):
    @staticmethod
    def gamma_list(seed, max_density, distribution_ceil, size):
        if distribution_ceil > max_density:
            raise DistributionCeilException('Distribution cell can not be higher than maximum density.')
        random.seed(seed)
        return [random.randint(1,distribution_ceil) for i in range(0, size)]

    @staticmethod
    def get_pixel_list_for_stego_data(img, max_density, distribution_ceil, seed):
        all_pixels = []
        for y in range(img.height):
            for x in range(img.width):
                all_pixels.append((x, y))
        stego_pixels = all_pixels[12:]
        gamma_size = len(stego_pixels) // max_density
        gamma = BMPLSBInterval.gamma_list(seed, max_density, distribution_ceil, gamma_size)[::-1]
        i = 0
        stego_pixels_cut = []
        while gamma:
            stego_step = gamma.pop()
            stego_pixels_cut.append(stego_pixels[i+stego_step])
            i = i+stego_step
        return stego_pixels_cut

    @staticmethod
    def put_stego(img, stego_data, seed, ceil, depth=1) :
        stego_data_len = len(stego_data)

        if (depth != 1) ^ (depth != 2) ^ (depth != 4):
            raise DepthException('Depth is not equal to 1, 2 or 4 bits.')

        if (img.height * img.width) < 24:
            raise ImageTooSmallException('Image is too small to contain header.')

        max_stego_size = BMPLSBInterval.calc_max_stego_data_size(img, depth)
        if stego_data_len > max_stego_size:
            raise StegomessageSizeException('Stegomessage is too long.')

        max_stego_density = BMPLSBInterval.calc_max_stego_density(img, stego_data_len, depth)
        BMPLSBInterval.put_header(img, stego_data)
        BMPLSBInterval.put_stego_data(max_stego_density, depth, img, stego_data, ceil, seed)
        return img

    @staticmethod
    def get_stego(img, seed, ceil, depth=1):
        if (depth != 1) ^ (depth != 2) ^ (depth != 4):
            raise DepthException('Depth is not equal to 1, 2 or 4 bits.')

        if (img.height * img.width) < 24:
            raise ImageTooSmallException('Image is too small to contain header.')

        stego_bytes_size = BMPLSBInterval.get_header(img)

        max_stego_size = BMPLSBInterval.calc_max_stego_data_size(img, depth)
        if stego_bytes_size > max_stego_size:
            raise StegomessageSizeException('Depth is too small to extract stegomessage of this size from image.')

        max_stego_density = BMPLSBInterval.calc_max_stego_density(img, stego_bytes_size, depth)

        stego_data = BMPLSBInterval.get_stego_data(max_stego_density, depth, img, stego_bytes_size, ceil, seed)

        return stego_data

    @staticmethod
    def put_stego_data(max_density, depth, img, stego_data, ceil, seed):
        stego_pixels = BMPLSBInterval.get_pixel_list_for_stego_data(img, max_density, ceil, seed)
        sliced_stego_data = BMPLSBInterval.slice_stego_data(stego_data, depth)
        BMPLSBInterval.write_to_pixels(img, stego_pixels, sliced_stego_data)

    @staticmethod
    def get_stego_data(max_density, depth, img, stego_bytes_size, ceil, seed):
        stego_data_pixels_list = BMPLSBInterval.get_pixel_list_for_stego_data(img, max_density, ceil, seed)
        stego_data = BMPLSB.get_from_pixels(img, stego_data_pixels_list, stego_bytes_size, depth)
        return stego_data
