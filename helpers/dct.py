from helpers.exceptions import DCTDimensionException
from helpers.array_slicer import *
from file_io.bmpimage import BMPImage
import math


coeff_array = [[1.0, 0.980785, 0.92388, 0.83147, 0.707107, 0.55557, 0.382683, 0.19509],
                   [1.0, 0.83147, 0.382683, -0.19509, -0.707107, -0.980785, -0.92388, -0.55557],
                   [1.0, 0.55557, -0.382683, -0.980785, -0.707107, 0.19509, 0.92388, 0.83147],
                   [1.0, 0.19509, -0.92388, -0.55557, 0.707107, 0.83147, -0.382683, -0.980785],
                   [1.0, -0.19509, -0.92388, 0.55557, 0.707107, -0.83147, -0.382683, 0.980785],
                   [1.0, -0.55557, -0.382683, 0.980785, -0.707107, -0.19509, 0.92388, -0.83147],
                   [1.0, -0.83147, 0.382683, 0.19509, -0.707107, 0.980785, -0.92388, 0.55557],
                   [1.0, -0.980785, 0.92388, -0.83147, 0.707107, -0.55557, 0.382683, -0.19509]]


def DCT(img):
    if (img.width % 8 != 0) | (img.height % 8 != 0):
        raise DCTDimensionException
        return 0

    channels = [slice_into_subarrays(channel) for channel in img.decompose_to_channels()]

    for channel in channels:
        for y_arr in range(len(channel)):
            for x_arr in range(len(channel[0])):
                subarray = channel[y_arr][x_arr]
                subarray_dct = forward_transform_block(subarray)
                channel[y_arr][x_arr] = subarray_dct

    return channels


def IDCT(channels, img):
    restored_img = BMPImage(img.export())
    for channel in channels:
        for y_arr in range(len(channel)):
            for x_arr in range(len(channel[0])):
                subarray = channel[y_arr][x_arr]
                subarray_res = inverse_transform_block(subarray)
                channel[y_arr][x_arr] = subarray_res
    merged_channels = [merge_from_subarrays(channel) for channel in channels]
    restored_img.compose_from_channels(merged_channels)

    return restored_img


def visualDCT(channels, img):
    vis_img = BMPImage(img.export())
    for channel in channels:
        maxv = float('-inf')
        minv = float('inf')
        for y in range(img.height):
            for x in range(img.width):
                if channel[y][x] > maxv:
                    maxv = channel[y][x]
                if channel[y][x] < minv:
                    minv = channel[y][x]
        for y in range(img.height):
            for x in range(img.width):
                pix = math.floor(((channel[y][x]-minv)/(maxv-minv))*255)
                if pix > 255:
                    pix = 255
                if pix < 0:
                    pix = 0
                channel[y][x]=pix

    vis_img.compose_from_channels(channels)
    return vis_img


def A(k):
    if k == 0:
        return math.sqrt(0.5)
    else:
        return 1


def forward_transform_block(block):
    dct_block = [[0 for x in range(8)] for y in range(8)]
    for v in range(8):
        for u in range(8):
            row = []
            for x in range(8):
                col = []
                for y in range(8):
                    col.append(block[y][x]*coeff_array[x][u]*coeff_array[y][v])
                row.append(sum(col))
            dct_block[v][u] = (1/4)*A(v)*A(u)*sum(row)
    return dct_block


def inverse_transform_block(dct_block):
    block = [[0 for x in range(8)] for y in range(8)]
    for y in range(8):
        for x in range(8):
            row = []
            for u in range(8):
                col = []
                for v in range(8):
                    col.append(A(u)*A(v)*dct_block[v][u]*coeff_array[x][u]*coeff_array[y][v])
                row.append(sum(col))
            pix = sum(row)/4
            block[y][x] = round(pix)
    return block




