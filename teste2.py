import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

import utils

original = cv.imread("./images/gabarito.jpeg") # 0 seta a leitura para grayscale
original = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
imgThresh = cv.threshold(original, 150,255,cv.THRESH_BINARY_INV)[1] # com um valor mais basixo pra thresh não perde muita coisa da parte de baixo
# original = cv.medianBlur(original, 5)
# th1 = cv.adaptiveThreshold(original,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,7)

# hist_original = cv.calcHist([original], [0], None, [256],[0,256])
# plt.plot(hist_original)
# print(hist_original)

cv.imshow('original', original)
cv.imshow('imgThresh', imgThresh)

utils.splitFullImage(imgThresh)
# cv.imshow('adpt gaussian', th1)
# plt.hist(hist_original, 256)
# plt.show()


cv.waitKey()
cv.destroyAllWindows()