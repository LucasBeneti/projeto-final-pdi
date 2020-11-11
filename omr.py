import numpy as np
import cv2
from matplotlib import pyplot as plt

import utils

original = cv2.imread("./images/gabarito.jpeg") # 0 seta a leitura para grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
imgThresh = cv2.threshold(original, 150,255,cv2.THRESH_BINARY_INV)[1] # com um valor mais basixo pra thresh não perde muita coisa da parte de baixo
# original = cv.medianBlur(original, 5)
# th1 = cv.adaptiveThreshold(original,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,7)

# hist_original = cv.calcHist([original], [0], None, [256],[0,256])
# plt.plot(hist_original)
# print(hist_original)

cv2.imshow('original', original)
cv2.imshow('imgThresh', imgThresh)


fullTestSplit = utils.splitFullImage(imgThresh)
nonZeroArr = utils.getArrayOfNonZeros(fullTestSplit)
finalAnsArr = utils.getAnsForEachQuestion(nonZeroArr)
print(finalAnsArr)


cv2.waitKey()
cv2.destroyAllWindows()