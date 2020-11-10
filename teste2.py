import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

original = cv.imread("./images/gabarito.jpeg",0) # 0 seta a leitura para grayscale
th1 = cv.adaptiveThreshold(original,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,7)

hist_original = cv.calcHist([original], [0], None, [256],[0,256])


cv.imshow('original', original)
cv.imshow('adpt gaussian', th1)




cv.waitKey()
cv.destroyAllWindows()