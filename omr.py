import numpy as np
import cv2
from matplotlib import pyplot as plt

import utils
import imageProcessing

# load das imagens
gabaritoImg = cv2.imread('./images/gabarito_1.jpeg')
testImg = cv2.imread('./images/48_anulada.jpeg')

thresh_val = 85 # valor semi arbitrário, não  pode ser muito maior pois 
# binarização é prejudicada caso a imagem tenha sombra, por isso
# só podemos aceitar até certo ponto de quantidade de sombra
gabaritoImg = cv2.cvtColor(gabaritoImg, cv2.COLOR_BGR2GRAY)
testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)

otsu_gabarito = imageProcessing.preprocessImages(gabaritoImg, thresh_val)
cv2.imshow('gabarito otsu',otsu_gabarito)
otsu_test = imageProcessing.preprocessImages(testImg, thresh_val)
cv2.imshow('teste otsu', otsu_test)

# funcão pra pegar a resposta final da imagem
# def getFileAns(img):
#     fullTestSplit = utils.splitFullImage(img)
#     nonZeroArr = utils.getArrayOfNonZeros(fullTestSplit)
#     finalAnsArr = utils.getAnsForEachQuestion(nonZeroArr)

#     return finalAnsArr


gabaritoAns = utils.getFileAns(otsu_gabarito)
testAns = utils.getFileAns(otsu_test)

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