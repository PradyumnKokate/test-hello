import base64
from PIL import Image
from io import BytesIO
import re
import numpy as np


# Decoding the encoded base64 string
def base64_webp_to_png(base64_string):
    # Convert base64 encoded string to bytes
    data = base64.b64decode(base64_string)

    # Read the bytes
    image = BytesIO(data)

    # Convert bytes into numpy array
    with Image.open(image) as img:
       img_array = np.array(img)

    # Numpy array to image
    img = Image.fromarray(img_array)

    return img
