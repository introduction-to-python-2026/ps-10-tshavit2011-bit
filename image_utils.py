from PIL import Image
import numpy as np
from scipy.signal import convolve2d


def load_image(path):
    # load image using PIL
    image = Image.open(path)

    # convert to numpy array
    image = np.array(image)

    # invert colors
    image = 255 - image

    return image


def edge_detection(image):
    # convert to grayscale if image is RGB
    if len(image.shape) == 3:
        gray = np.mean(image, axis=2)
    else:
        gray = image

    # Sobel filters
    filter_x = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    filter

    
