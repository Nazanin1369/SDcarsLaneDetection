import imageUtil as imgUtil
import colorSelection as cs
import regionOfInterest as rgn
import cannedEdgeDetection as can
import houghTransform as ht


def defineLanesWithColor(image, name, r, g, b):
    # Make a copy of image
    color_select = imgUtil.copyImage(image)

    # Mask pixels below the threshold
    color_thresholds = cs.setColorThresholds(image, color_select, r, g, b)

    #Save image
    imgUtil.displayAndSaveImage(color_select, './imgs/' + name + '-color-lane-selection.jpg')

    return color_select



def defineLanesWithRegion(image, name, r, g, b):
    # Make a copy of image
    region_select = imgUtil.copyImage(image)
    color_select = imgUtil.copyImage(image)

    # Find the region inside the lines
    color_thresholds = cs.setColorThresholds(image, color_select, r, g, b)
    region_thresholds = rgn.defineRegionOfInterest(image)

    # Find where image is both colored right and in the region
    region_select[~color_thresholds & region_thresholds] = [255,0,0]

    #Save image
    imgUtil.displayAndSaveImage(region_select, './imgs/' + name + '-region-lane-selection.jpg')

    return region_select


def defineLanesWithColorAndRegion(image, name, r, g, b):
    # Make a copy of image
    color_select = imgUtil.copyImage(image)
    region_select = imgUtil.copyImage(image)

    # Mask pixels below the threshold
    color_thresholds = cs.setColorThresholds(image, color_select, r, g, b)

    # Find the region inside the lines
    region_thresholds = rgn.defineRegionOfInterest(image)


    # Mask color and region selection
    region_color_select = imgUtil.copyImage(color_select)
    region_color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]

    imgUtil.displayAndSaveImage(region_color_select, './imgs/' + name + '-region-color-lane-selection.jpg')

    return region_color_select



def defineLanesWithCanny(image, name, save):
    # Make a copy of image
    grayed_select = imgUtil.copyImage(image)

     # Generate Gray scaled image
    grayed_select = can.grayOutImage(grayed_select)

    # Applied Canny function to grayed scale image to find out edges of gradiants
    edge_select = can.cannedImage(grayed_select)

    if save:
        imgUtil.saveImageWithCmap(grayed_select, './imgs/' + name + '-grayed-out-lane-selection.jpg', cmap='gray')
        imgUtil.saveImageWithCmap(edge_select, './imgs/' + name + '-edge-select-lane-selection.jpg', cmap='Greys_r')

    return edge_select



def defineLanesWithHoughTransform(image, name):
    edges = defineLanesWithCanny(image, name, False)
    hough_transformed_select = ht.houghTransform(image, edges)
    imgUtil.displayAndSaveImage(hough_transformed_select, './imgs/' + name + '-hough-transform-lane-selection.jpg')


def defineLanesWithHoughTransformAndRegionInterest(image, name):
    edges = defineLanesWithCanny(image, name, False)
    hough_transformed_select = ht.houghTransformAndRegionSelect(image, edges)
    imgUtil.displayAndSaveImage(hough_transformed_select, './imgs/' + name + '-hough-transform-region-lane-selection.jpg')
##########################################

# read images
image1 = imgUtil.readImage('./imgs/lane.jpg')
image2 = imgUtil.readImage('./imgs/exit-ramp.jpg')

defineLanesWithColor(image1, 'img1', 200, 200, 200)
defineLanesWithRegion(image1, 'img1', 200, 200, 200)
defineLanesWithColorAndRegion(image1, 'img1', 200, 200, 200)
defineLanesWithCanny(image1, 'img1', True)--#

defineLanesWithColor(image2, 'img2', 150, 90, 10)
defineLanesWithRegion(image2, 'img2', 150, 90, 10)
defineLanesWithColorAndRegion(image2, 'img2', 50, 90, 10)
defineLanesWithCanny(image2, 'img2', True)
defineLanesWithHoughTransform(image2, 'img2')
defineLanesWithHoughTransformAndRegionInterest(image2, 'img2')
########################################