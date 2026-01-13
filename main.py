import numpy as np
from skimage.filters import median
from skimage.morphology import ball
from skimage import io

from image_utils import load_image, edge_detection


# load image
image = load_image("image.png")

# noise suppression
clean_image = median(image, ball(3))

# edge detection
edges = edge_detection(clean_image)

# save result
io.imsave("edges.png", edges / edges.max())
