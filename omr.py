import numpy as np
import cv2
from matplotlib import pyplot as plt

import utils

# load das imagens
gabaritoImg = cv2.imread('./images/gabarito_1.jpeg')
testImg = cv2.imread('./images/prova_1.jpeg')


# um ponto a melhorar é o threshhold, porque está muito arbitrário, dar uma olhada
# se rola fazer calculando o histograma e obter um valor melhor
gabaritoImg = cv2.cvtColor(gabaritoImg, cv2.COLOR_BGR2GRAY)
gabaritoThresh = cv2.threshold(gabaritoImg, 90,255,cv2.THRESH_BINARY_INV)[1]
testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
testThresh = cv2.threshold(testImg, 90,255,cv2.THRESH_BINARY_INV)[1]

# funcão pra pegar a resposta final da imagem
def getFileAns(img):
    fullTestSplit = utils.splitFullImage(img)
    nonZeroArr = utils.getArrayOfNonZeros(fullTestSplit)
    finalAnsArr = utils.getAnsForEachQuestion(nonZeroArr)

    return finalAnsArr


gabaritoAns = getFileAns(gabaritoThresh)
testAns = getFileAns(testThresh)

print('Gabarito: ', len(gabaritoAns))
print('Prova corrigida: ', len(testAns))

# correção efetivamente sendo feita e depois um print do acerto
acertos = 0
for i in range(len(gabaritoAns)):
    if(testAns[i] == gabaritoAns[i]):
        acertos +=1

print('resultado final: ', acertos) # pelas minhas contas o teste deu certinho