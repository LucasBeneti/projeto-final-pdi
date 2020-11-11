import numpy as np
import cv2
from matplotlib import pyplot as plt

import utils
import imageProcessing

# load das imagens
gabaritoImg = cv2.imread('./images/gabarito_1.jpeg')
testImg = cv2.imread('./images/prova_1.jpeg')


# um ponto a melhorar é o threshhold, porque está muito arbitrário, dar uma olhada
# se rola fazer calculando o histograma e obter um valor melhor
thresh_val = 90
gabaritoImg = cv2.cvtColor(gabaritoImg, cv2.COLOR_BGR2GRAY)
# gabaritoThresh = cv2.threshold(gabaritoImg, thresh_val,255,cv2.THRESH_BINARY_INV)[1]
testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
# testThresh = cv2.threshold(testImg, thresh_val,255,cv2.THRESH_BINARY_INV)[1]

otsu_gabarito = imageProcessing.preprocessImages(gabaritoImg)
cv2.imshow('gabarito otsu',otsu_gabarito)
otsu_test = imageProcessing.preprocessImages(testImg)
cv2.imshow('teste otsu', otsu_test)

# utils.getImageHist(gabaritoImg)
# utils.getImageHist(testImg)

# hist_gabarito = cv2.calcHist([gabaritoImg],[0], None,[256],[0,256])
# hist_test = cv2.calcHist([testImg],[0], None,[256],[0,256])

# plt.subplot(121), plt.plot(hist_gabarito)
# plt.subplot(122), plt.plot(hist_test)
# plt.show()
# cv2.imshow('gabarito', gabaritoThresh)
# cv2.imshow('teste', testThresh)

# funcão pra pegar a resposta final da imagem
def getFileAns(img):
    fullTestSplit = utils.splitFullImage(img)
    nonZeroArr = utils.getArrayOfNonZeros(fullTestSplit)
    finalAnsArr = utils.getAnsForEachQuestion(nonZeroArr)

    return finalAnsArr


gabaritoAns = getFileAns(otsu_gabarito)
testAns = getFileAns(otsu_test)

print('Gabarito: ', gabaritoAns)
print('Prova corrigida: ', testAns)

# correção efetivamente sendo feita e depois um print do acerto
acertos = 0
for i in range(len(gabaritoAns)):
    if(testAns[i] == gabaritoAns[i]):
        acertos +=1

print('resultado final: ', acertos) # pelas minhas contas o teste deu certinho

cv2.waitKey(0)
cv2.destroyAllWindows()