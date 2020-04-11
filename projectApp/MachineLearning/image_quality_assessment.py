# https://pypi.org/project/image-quality/

import imquality.brisque as brisque
import PIL.Image
# from pathlib import Path
import cv2
# from django.core.files.storage import FileSystemStorage
import base64
import numpy as np
from PIL import Image
import io



def image_quality(image_path):

    # path for reading
    root = "djangoProject"
    path = root + image_path

    image = PIL.Image.open(path)
    result = brisque.score(image)

    #THE MEAN VALUE NEEDED TO B ASSIGNED
    # lower the number  = less pixelated
    # however, the blurry images do not work in this
    return result


# Take in base64 string and return cv image
# https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image/16214280
def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))

    numpy_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    return numpy_image
