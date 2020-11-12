import numpy as np
import cv2
from matplotlib import pyplot as plt

import utils
import imageProcessing

# load das imagens
gabaritoImg = cv2.imread('./images/novo_gabarito.jpeg')
testImg = cv2.imread('./images/nova_prova.jpeg')

thresh_val = 85 # valor semi arbitrário, não  pode ser muito maior pois 
# binarização é prejudicada caso a imagem tenha sombra, por isso
# só podemos aceitar até certo ponto de quantidade de sombra
gabaritoImg = cv2.cvtColor(gabaritoImg, cv2.COLOR_BGR2GRAY)
testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)

_gabarito = imageProcessing.preprocessImages(gabaritoImg, thresh_val)
cv2.imshow('gabarito ',_gabarito)
_test = imageProcessing.preprocessImages(testImg, thresh_val)
cv2.imshow('teste ', _test)

# checagem da questão que devia ser anulada
fullTestSplit = utils.splitFullImage(_test)
nonZeroArr = utils.getArrayOfNonZeros(fullTestSplit)
print('questao 22', nonZeroArr[21])
print('ans for question 22', utils.chooseAnswerForQuestion(nonZeroArr[21]))
finalAnsArr = utils.getAnsForEachQuestion(nonZeroArr)