import cv2
import math
import entropy
import scale as sc
import numpy as np,sys

def init():
    img = cv2.imread('/home/atlanticolab/Imagens/lena512.bmp')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tmp = img.copy()
    
    cv2.namedWindow('image')
    
    while(1):
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            exit() 
        if k == ord('o'):
            pyramid = [tmp]
            for i in xrange(6):
                tmp = cv2.pyrDown(tmp)
                tmp = gaussianBlur(tmp)
                pyramid.append(tmp)
            showAll(pyramid)
        if k == ord('p'):
            pyramid = [tmp]
            for i in xrange(2):
                tmp = cv2.pyrUp(tmp)
                pyramid.append(tmp)
            showAll(pyramid)
        if k == ord('d'):
            pyramid = [tmp]
            for i in xrange(5):
                tmp = sc.prymeDown(tmp)
                pyramid.append(tmp)
            showAll(pyramid)        

def showAll(pryramid):
    for image in pryramid:
        cv2.imshow("Pry {}".format(np.random.random_sample()), image)
        print(entropy.calc(image))
        
def gaussianBlur(img):
    return cv2.GaussianBlur(img, (5,5), 0)
                       
init()        