import numpy as np
from image_utils import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import ball
from PIL import Image


# load image
image = load_image("image.png")

# noise suppression
clean_image = median(image, ball(3))

# edge detection
edgeMAG = edge_detection(clean_image)

# binary conversion (threshold)
threshold = np.mean(edgeMAG)
edge_binary = edgeMAG > threshold

# save result
edge_image = Image.fromarray(edge_binary.astype(np.uint8) * 255)
edge_image.save("my_edges.png")

