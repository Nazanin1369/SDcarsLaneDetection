import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Define image path
image_path = './imgs/lane.jpg'

# Define color selection criteria
red_threshold = 200
green_threshold = 200
blue_threshold = 200

# Read in the image
image = mpimg.imread(image_path)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)

# set thresholds
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

print (image)
# Do a boolean or with the "|" character to identify
# pixels below the thresholds
thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])

print ((image[:,:,0] < rgb_threshold[0]), rgb_threshold)
color_select[thresholds] = [0,0,0]
plt.imshow(color_select)
# Display the image
plt.imshow(color_select)

# save the image
mpimg.imsave("./imgs/lane-color-selection.jpg", color_select)
