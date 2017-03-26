import cv2
import math
import numpy as np

def prymeDown(image):
    height, width = image.shape[:2]
    size = (width, height, 1)
    nImage = np.zeros(size, np.int8)
    
    for col in range(2, len(image), 2):
        for row in range(2, len(image[col]), 2):    
            nImage[col / 2][row / 2] = image[col][row] / 2
    return nImage
    
    