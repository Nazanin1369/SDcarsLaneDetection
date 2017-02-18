import imageUtil as imgUtil
import colorSelection as cs
import regionOfInterest as rgn

# read the image
image = imgUtil.readImage('./imgs/lane.jpg')

# Make a copy of image
color_select = imgUtil.copyImage(image)
region_select = imgUtil.copyImage(image)

# Mask pixels below the threshold
color_thresholds = cs.setColorThresholds(image, color_select)

# Find the region inside the lines
region_thresholds = rgn.defineRegionOfInterest(image)

region_color_select = imgUtil.copyImage(color_select)
region_color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]
# Find where image is both colored right and in the region
region_select[~color_thresholds & region_thresholds] = [255,0,0]

#Save image
imgUtil.displayAndSaveImage(color_select, './imgs/color-lane-selection.jpg')
imgUtil.displayAndSaveImage(region_select, './imgs/region-lane-selection.jpg')
imgUtil.displayAndSaveImage(region_color_select, './imgs/region-color-lane-selection.jpg')

