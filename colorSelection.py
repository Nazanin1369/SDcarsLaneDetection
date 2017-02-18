import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def setColorThresholds(image, image_copy, red_threshold=200, green_threshold=200, blue_threshold=200):
    # set thresholds
    rgb_threshold = [red_threshold, green_threshold, blue_threshold]

    # Do a boolean or with the "|" character to identify
    # pixels below the thresholds
    color_thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])
    image_copy[color_thresholds] = [0,0,0]
    return color_thresholds

