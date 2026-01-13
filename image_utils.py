from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    pass # Replace the `pass` with your code

def edge_detection(image):
 import numpy as np
from skimage import io
from scipy.signal import convolve2d

def load_image(path):
    """
    Loads an image, converts it to numpy array and inverts colors
    """
    image = io.imread(path)
    image = np.array(image)
    image = 255 - image
    return image


def edge_detection(image):
    """
    Receives an image array and returns edge magnitude image
    """

    # convert to grayscale if needed
    if len(image.shape) == 3:
        gray = np.mean(image, axis=2)
    else:
        gray = image

    # Sobel filters
    filter_x = np.ar_

    
