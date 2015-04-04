from math import log10
from helpers.exceptions import ImageDimensionsException


def calculate_MSE(img_a, img_b):
        img_a_dim = img_a.width, img_a.height
        img_b_dim = img_b.width, img_a.height
        if img_a_dim != img_b_dim:
            raise ImageDimensionsException("The images are not the same size. Cannot compare!")
            return 0

        pixcount = img_a_dim[0] * img_a_dim[1]

        dev_R, dev_G, dev_B = calculate_deviation(img_a, img_b)

        MSE_R, MSE_G, MSE_B = dev_R * (1/pixcount), dev_G * (1/pixcount), dev_B * (1/pixcount)

        return (MSE_R+MSE_G+MSE_B)/3


def calculate_deviation(img_a, img_b):
    img_a_dim = img_a.width, img_a.height
    dev_R = 0
    dev_G = 0
    dev_B = 0

    for y in range(img_a_dim[1]):
        for x in range(img_a_dim[0]):
            img_a_pixel = img_a.get_pixel((x, y))
            img_b_pixel = img_b.get_pixel((x, y))
            dev_R += (img_a_pixel[2] - img_b_pixel[2]) ** 2
            dev_G += (img_a_pixel[1] - img_b_pixel[1]) ** 2
            dev_B += (img_a_pixel[0] - img_b_pixel[0]) ** 2

    return dev_R, dev_G, dev_B


def calculate_mean(img_a):
    return calculate_deviation(img_a, img_a.return_dummy())


def calculate_PSNR(img_a, img_b, calculated_mse=None):
        if calculated_mse is None:
            calculated_mse = calculate_MSE(img_a, img_b)
        return 10 * log10((255**2) / calculated_mse)


def calculate_NMSE(img_a, img_b, calculated_mse=None):
    if calculated_mse is None:
        calculated_mse = calculate_MSE(img_a, img_b)
    mse_img_a = calculate_MSE(img_a, img_b.return_dummy())
    return calculated_mse / mse_img_a


def calculate_SNR(img_a, img_b):
    return 10 * log10(((sum(calculate_mean(img_a)) / 3) / (sum(calculate_deviation(img_a, img_b)) / 3)))
