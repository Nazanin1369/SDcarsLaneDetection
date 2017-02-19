import imageUtil as imgUtil
import colorSelection as cs
import regionOfInterest as rgn
import cannedEdgeDetection as can

# read images
image1 = imgUtil.readImage('./imgs/lane.jpg')
image2 = imgUtil.readImage('./imgs/exit-ramp.jpg')


def defineLanes(image, name):
    # Make a copy of image
    color_select = imgUtil.copyImage(image)
    region_select = imgUtil.copyImage(image)
    grayed_select = imgUtil.copyImage(image)

    # Mask pixels below the threshold
    color_thresholds = cs.setColorThresholds(image, color_select)

    # Find the region inside the lines
    region_thresholds = rgn.defineRegionOfInterest(image)

    # Mask color and region selection
    region_color_select = imgUtil.copyImage(color_select)
    region_color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]

    # Find where image is both colored right and in the region
    region_select[~color_thresholds & region_thresholds] = [255,0,0]

    # Generate Gray scaled image
    grayed_select = can.grayOutImage(grayed_select)

    # Applied Canny function to grayed scale image to find out edges of gradiants
    edge_select = can.cannedImage(grayed_select)

    #Save image
    imgUtil.displayAndSaveImage(color_select, './imgs/' + name + 'color-lane-selection.jpg')
    imgUtil.displayAndSaveImage(region_select, './imgs/' + name + 'region-lane-selection.jpg')
    imgUtil.displayAndSaveImage(region_color_select, './imgs/' + name + 'region-color-lane-selection.jpg')
    imgUtil.saveImageWithCmap(grayed_select, './imgs/' + name + 'grayed-out-lane-selection.jpg', cmap='gray')
    imgUtil.saveImageWithCmap(edge_select, './imgs/' + name + 'edge-select-lane-selection.jpg', cmap='Greys_r')


#defineLanes(image1, 'img1')

defineLanes(image2, 'img2')