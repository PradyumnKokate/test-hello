# if data == data3 :
#     print("multiple")

# print(data3.isascii())

# def is_multiple_of_4(s):
#     return len(s) % 4 == 0

# if is_multiple_of_4(data3):
#     print("The string length is a multiple of 4.")
# else:
#     print("The string length is not a multiple of 4.")

# number_of_characters = len(data3)
# print(number_of_characters)

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

# The the query parameter (base64 encoded string)
#img_query = st.query_params.get('img_str')

# if img_query is not None:

#   # Replace special characters into their usual characters
#   img_query = img_query.replace('-', '+')
#   img_query = img_query.replace('_', '/')
#   img_query = img_query.replace('.', '=')

#   image_from_query = base64_webp_to_png(img_query)

#   # Save the user input image with a path
#   image_from_query.save('user_input.png’)