import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def readImage(path):
    # Read in the image
    image = mpimg.imread(path)

    # Grab the x and y size and make a copy of the image
    ysize = image.shape[0]
    xsize = image.shape[1]
    return image


def copyImage(image):
    color_select = np.copy(image)
    return color_select


def displayAndSaveImage(img, path):
    plt.imshow(img)
    mpimg.imsave(path, img)