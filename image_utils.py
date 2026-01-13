from PIL import Image
import numpy as np
from scipy.signal import convolve2d


def load_image(path):
    image = Image.open(path)
    image = np.array(image)
    return image


def edge_detection(image):
    # convert to grayscale by averaging channels
    if len(image.shape) == 3:
        gray = np.mean(image, axis=2)
    else:
        gray = image

    kernelY = np.array([
        [ 1,  2,  1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ])

    kernelX = np.array([
        [ 1,  0, -1],
        [ 2,  0, -2],
        [ 1,  0, -1]
    ])

    edgeY = convolve2d(gray, kernelY, mode="same", boundary="fill", fillvalue=0)
    edgeX = convolve2d(gray, kernelX, mode="same", boundary="fill", fillvalue=0)

    edgeMAG = edgeX**2 + edgeY**2

    return edgeMAG
