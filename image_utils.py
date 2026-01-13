from PIL import Image
import numpy as np
from scipy.signal import convolve2d


def load_image(path):
    # read image
    image = Image.open(path)

    # convert to numpy array
    image = np.array(image)

    return image


def edge_detection(image):
    # convert to grayscale if needed
    if len(image.shape) == 3:
        gray = np.mean(image, axis=2)
    else:
        gray = image

    # filters (Sobel)
    filter_x = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    filter_y = np.array([
        [1,  2,  1],
        [0,  0,  0],
        [-1, -2, -1]
    ])

    edgeX = convolve2d(gray, filter_x, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(gray, filter_y, mode='same', boundary='fill', fillvalue=0)

    edgeMAG = edgeX**2 + edgeY**2

    return edgeMAG

