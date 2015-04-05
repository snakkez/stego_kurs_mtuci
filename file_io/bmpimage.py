from .image import Image


class BMPImage(Image):
    def __init__(self, file_bytes):
        self.header = bytearray(file_bytes[:54])
        self.data = bytearray(file_bytes[54:])
        self.size = int.from_bytes(file_bytes[2:6], 'little')
        self.width = int.from_bytes(file_bytes[18:22], 'little')
        self.height = int.from_bytes(file_bytes[22:26], 'little')
        row_byte_len = self.width*3
        padding = (4 - (row_byte_len % 4)) % 4
        self.row_offset = row_byte_len + padding


    def return_dummy(self):
        dummy = BMPImage(self.export())
        for y in range(dummy.height):
            for x in range(dummy.width):
                dummy.set_pixel((x, y), bytearray([0, 0, 0]))
        return dummy

    def get_pixel_offset(self, pos, raw=False):
        x, y = pos
        if not raw:
            y = self.height - y - 1
        return (x*3)+self.row_offset*y, (x*3)+3+self.row_offset*y

    def get_pixel(self, pos, raw=False):
        start, end = self.get_pixel_offset(pos, raw)
        return self.data[start:end]

    def set_pixel(self, pos, pixel, raw=False):
        start, end = self.get_pixel_offset(pos, raw)
        self.data[start:end] = pixel

    def decompose_to_channels(self):
        r_channel = [[self.get_pixel((x, y))[2] for x in range(0, self.height)] for y in range(0, self.width)]
        g_channel = [[self.get_pixel((x, y))[1] for x in range(0, self.height)] for y in range(0, self.width)]
        b_channel = [[self.get_pixel((x, y))[0] for x in range(0, self.height)] for y in range(0, self.width)]
        return b_channel, g_channel, r_channel

    def compose_from_channels(self, channels):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.set_pixel((x,y), bytearray((channels[0][y][x], channels[1][y][x], channels[2][y][x])))
        return 0

    def decompose_to_binary_channels(self):
        r_channel = [[format(self.get_pixel((x, y))[2], '08b') for x in range(0, self.height)] for y in range(0, self.width)]
        g_channel = [[format(self.get_pixel((x, y))[1], '08b') for x in range(0, self.height)] for y in range(0, self.width)]
        b_channel = [[format(self.get_pixel((x, y))[0], '08b') for x in range(0, self.height)] for y in range(0, self.width)]
        return b_channel, g_channel, r_channel

    def compose_from_binary_channels(self, channels):
        for y in range(0, self.height):
            for x in range(0, self.width):
                b = int(channels[0][y][x], 2)
                g = int(channels[1][y][x], 2)
                r = int(channels[2][y][x], 2)
                self.set_pixel((x, y), bytearray((b, g, r)))
        return 0

    def export(self):
        return self.header + self.data