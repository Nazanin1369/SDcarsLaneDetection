import cv2

print(cv2.__version__)

# grayscale conversion
def grayOutImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray


def cannedImage(grayedImage, kernel_size=3, low_threshold=50, high_threshold=90):
    # Define a kernel size for Gaussian smoothing / blurring
    blur_gray = cv2.GaussianBlur(grayedImage,(kernel_size, kernel_size), 0)
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    return edges


