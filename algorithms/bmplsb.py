from .stegoalogrithm import StegoAlgorithm


class BMPLSBDepthException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class BMPLSBDensityException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class BMPLSBStegomessageSizeException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class BMPLSBNoHeaderFoundException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class BMPLSBImageTooSmallException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)


class BMPLSB(StegoAlgorithm):
    @staticmethod
    def calc_max_stego_data_size(img, depth):
        return ((img.height * img.width - 12) * depth * 3) // 8

    @staticmethod
    def calc_max_stego_density(img, stego_data_len, depth):
        return ((img.height * img.width - 12) * 3) // (stego_data_len * (8 // depth))

    @staticmethod
    def byte_slice(byte, depth):
        return [byte[i:i+depth] for i in range(0, len(byte), depth)]

    @staticmethod
    def slice_stego_data(stego_data, depth):
        sliced_stego = []
        for byte in stego_data:
            bin_byte = format(byte, '08b')
            sliced_stego += BMPLSB.byte_slice(bin_byte, depth)
        return sliced_stego

    @staticmethod
    def put_header(img, stego_data):
        header = bytearray('LSB', 'ascii') + len(stego_data).to_bytes(3, 'little')
        sliced_header = BMPLSB.slice_stego_data(header, 4)
        pixels_for_header = BMPLSB.get_first_n_pixels_list(img, 12)
        BMPLSB.write_to_pixels(img, pixels_for_header, sliced_header)

    @staticmethod
    def get_first_n_pixels_list(img, n):
        pixels = []
        for y in range(img.height):
            for x in range(img.width):
                pixels.append((x, y))
                if len(pixels) >= n:
                    return pixels

    @staticmethod
    def write_to_pixels(img, pixel_list, sliced_stego_data):
        channels = img.decompose_to_channels()
        for channel in channels:
            for x, y in pixel_list:
                try:
                    stego_slice = sliced_stego_data.pop(0)
                    stego_len = len(stego_slice)
                    data_byte = channel[y][x][:8-stego_len]+stego_slice
                    channel[y][x] = data_byte
                except IndexError:
                    img.compose_from_channels(channels)
                    return True

    @staticmethod
    def get_from_pixels(img, pixel_list, bytes_n, depth):
        bytes = []
        buffer = ''
        channels = img.decompose_to_channels()
        for channel in channels:
            if len(bytes) == bytes_n:
                    return bytearray([int(byte, 2) for byte in bytes])
            for x, y in pixel_list:
                if len(bytes) == bytes_n:
                    return bytearray([int(byte, 2) for byte in bytes])
                if len(buffer) == 8:
                    bytes.append(buffer)
                    buffer = ''
                pixel = channel[y][x]
                buffer += pixel[8-depth:]



    @staticmethod
    def get_pixel_list_for_stego_data(img, density):
        all_pixels = []
        for y in range(img.height):
            for x in range(img.width):
                all_pixels.append((x, y))
        stego_pixels = all_pixels[12:]
        stego_pixels_cut = [stego_pixels[i] for i in range(0, len(stego_pixels), density)]
        return stego_pixels_cut

    @staticmethod
    def put_stego_data(density, depth, img, stego_data):
        stego_pixels = BMPLSB.get_pixel_list_for_stego_data(img, density)
        sliced_stego_data = BMPLSB.slice_stego_data(stego_data, depth)
        BMPLSB.write_to_pixels(img, stego_pixels, sliced_stego_data)

    @staticmethod
    def put_stego(img, stego_data, depth=1, density=None):
        stego_data_len = len(stego_data)

        if (depth != 1) ^ (depth != 2) ^ (depth != 4):
            raise BMPLSBDepthException('Depth is not equal to 1, 2 or 4 bits.')

        if (img.height * img.width) < 24:
            raise BMPLSBImageTooSmallException('Image is too small to contain header.')

        max_stego_size = BMPLSB.calc_max_stego_data_size(img, depth)
        if stego_data_len > max_stego_size:
            raise BMPLSBStegomessageSizeException('Stegomessage is too long.')

        max_stego_density = BMPLSB.calc_max_stego_density(img, stego_data_len, depth)

        if density == None:
            density = max_stego_density
        elif density > max_stego_density:
            raise BMPLSBDensityException("Density is too big. Maximum density is " + str(max_stego_density))
        elif density <= 0:
            raise BMPLSBDensityException("Density cannot be smaller than 0.")
        BMPLSB.put_header(img, stego_data)

        BMPLSB.put_stego_data(density, depth, img, stego_data)

        stego_params = {'stego_data_length': stego_data_len, 'depth': depth, 'density': density}

        return img, stego_params

    @staticmethod
    def get_header(img):
        correct_header_flag = bytearray([76, 83, 66])
        pixels_for_header = BMPLSB.get_first_n_pixels_list(img, 12)
        header_bytes = BMPLSB.get_from_pixels(img, pixels_for_header, 6, 4)
        if header_bytes[:3] != correct_header_flag:
            raise BMPLSBNoHeaderFoundException('No header found!')
        stego_bytes_size = int.from_bytes(header_bytes[3:], 'little')
        return stego_bytes_size


    @staticmethod
    def get_stego_data(density, depth, img, stego_bytes_size):
        stego_data_pixels_list = BMPLSB.get_pixel_list_for_stego_data(img, density)
        stego_data = BMPLSB.get_from_pixels(img, stego_data_pixels_list, stego_bytes_size, depth)
        return stego_data

    @staticmethod
    def get_stego(img, depth=1, density=1):
        if (depth != 1) ^ (depth != 2) ^ (depth != 4):
            raise BMPLSBDepthException('Depth is not equal to 1, 2 or 4 bits.')

        if (img.height * img.width) < 24:
            raise BMPLSBImageTooSmallException('Image is too small to contain header.')

        stego_bytes_size = BMPLSB.get_header(img)

        max_stego_size = BMPLSB.calc_max_stego_data_size(img, depth)
        if stego_bytes_size > max_stego_size:
            raise BMPLSBStegomessageSizeException('Depth is too small to extract stegomessage of this size from image.')

        max_stego_density = BMPLSB.calc_max_stego_density(img, stego_bytes_size, depth)

        if density > max_stego_density:
            raise BMPLSBDensityException("Density is too big. Maximum density is " + str(max_stego_density))
        elif density <= 0:
            raise BMPLSBDensityException("Density cannot be smaller than 0.")

        stego_data = BMPLSB.get_stego_data(density, depth, img, stego_bytes_size)

        return stego_data




