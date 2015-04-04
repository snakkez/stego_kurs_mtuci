from helpers.exceptions import DCTDimensionException
from helpers.array_slicer import *
import math


def DCT(img):
    if (img.width % 8 != 0) | (img.heigth % 8 != 0):
        raise DCTDimensionException
        return 0
    b_channel, g_channel, r_channel = img.decompose_to_channels()
    b_channel_sliced = slice_into_subarrays(b_channel)
    g_channel_sliced = slice_into_subarrays(g_channel)
    r_channel_sliced = slice_into_subarrays(r_channel)

def C(i, j):
    if i == 0:
        return math.sqrt(1/8)
    else:
        return math.sqrt

def forward_transform(inp_matrix):
    transformed_matrix = inp_matrix


