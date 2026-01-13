import numpy as np
from skimage.filters import median
from skimage.morphology import ball
from skimage import io

from image_utils import load_image, edge_detection


# 1. load original image
image = load_image("image.png")  # שימי כאן את שם התמונה שלך

# 2. remove noise
clean_image = median(image, ball(3))

# 3. edge detection
edges = edge_detection(clean_image)

# 4. convert to binary image
threshold = np.mean(edges)
binary_edges = edges > threshold

# 5. save result
io.imsave("edges.png", binary_edges.astype(np.uint8) * 255)

