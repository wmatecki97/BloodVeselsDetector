import numpy as np
import matplotlib.pyplot as plt
from cv2 import bitwise_and, resize
from skimage.exposure import rescale_intensity, equalize_hist, equalize_adapthist
from skimage.filters import frangi, gaussian


def get_blood_vessels(image, mask):

    image = np.array(image)
    image = resize(image, None, fx=0.7, fy=0.7)
    mask = np.asarray(mask)
    mask = resize(mask, None, fx=0.7, fy=0.7)
    mask = mask[:, :, 1]

    # r=0 g b=0
    image[:, :, [0, 2]] = 0
    green = image[:, :, 1]

    green = contrast_stretching(green)
    # green = equalize_hist(green)

    green = frangi(green)

    # green = contrast_stretching(green)
    green = equalize_hist(green)


    green = np.asarray(green)
    # p = 0.06  # for contrast_stretching
    p = 0.92  # for equalize_hist
    print("sdsd")

    green[green > p] = 1
    green[green <= p] = 0

    res = bitwise_and(green, green, mask=mask)

    return res


def contrast_stretching(img):
    p1, p99 = np.percentile(img, (1, 99))
    img = rescale_intensity(img, in_range=(p1, p99))
    return img
