import cv2
import math
import numpy as np

def calc(img):
    #hist,_ = np.histogram(img, np.arange(0, 256), normed=True)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist = hist.ravel()/hist.sum()
    logs = np.log2(hist+0.00001)
    entropy = -1 * (hist*logs).sum()
    return entropy  
    
def calcHist(img):
    #histSize = 256
    #hist = cv2.calcHist([img],[0],None,[256],[0,256])
    hist = np.histogram(img, np.arange(0, 256), normed=True)
    return hist[1]
        
    