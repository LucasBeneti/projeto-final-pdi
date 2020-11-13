import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

import utils
import imageProcessing


def getRightAnswers(gabarito, prova):
    acertos = 0
    for i in range(len(gabaritoAns)):
        if(provaAns[i] == gabaritoAns[i]):
            acertos +=1
    return acertos

if __name__ == '__main__':
    print('Corretor de provas')
    print('O usuario deve passar os paths referentes as pastas das imagens dos gabaritos e depois o arquivo da prova a ser corrigida')
    # print('Dê o endereço da pasta onde os gabaritos estão contidos')
    imagesPaths = input('Pasta dos gabaritos: ') # pasta que tem todas as provas
    # os gabaritos precisam ter um nome específico nelas
    lista_files = os.listdir(imagesPaths);
    tiposGabaritos = {}
    for gabaritoPath in lista_files:
        tipo = gabaritoPath.split('.')[0][-1] # pega o numero que serve idenetificador do tipo
        if(imagesPaths[-1] == '/'):
            pathCompletoGabarito = imagesPaths + gabaritoPath
        else:
            pathCompletoGabarito = imagesPaths + '/' + gabaritoPath
        tiposGabaritos[tipo] = pathCompletoGabarito

    pathProvaRespondida = input('path para a prova: ')
    tipoRespondido = input('Tipo da prova respondida: ')
    # path certinho para imagem da prova
    pathProvaRespondida = os.path.abspath(pathProvaRespondida)
    pathGabaritoEscolhido = os.path.abspath(tiposGabaritos[tipoRespondido])

    # load das imagens
    gabaritoImage = cv2.imread(pathGabaritoEscolhido)
    print('path do gabarito: ', pathGabaritoEscolhido)
    provaImage = cv2.imread(pathProvaRespondida)
    print('path da prova: ', pathProvaRespondida)

    thresh_val = 85 # valor semi arbitrário, não  pode ser muito maior pois 
    # binarização é prejudicada caso a imagem tenha sombra, por isso
    # só podemos aceitar até certo ponto de quantidade de sombra
    cv2.imshow('Gabarito Original', gabaritoImage)
    gabaritoImage = cv2.cvtColor(gabaritoImage, cv2.COLOR_BGR2GRAY)
    provaImage = cv2.cvtColor(provaImage, cv2.COLOR_BGR2GRAY)

    gabaritoProcessed = imageProcessing.preprocessImages(gabaritoImage, thresh_val)
    cv2.imshow('Gabarito Processado',gabaritoProcessed)
    provaProcessed = imageProcessing.preprocessImages(provaImage, thresh_val)
    cv2.imshow('Prova Processada', provaProcessed)

    gabaritoAns = utils.getFileAns(gabaritoProcessed)
    provaAns = utils.getFileAns(provaProcessed)

    print('Respostas obtidas do gabarito: ', gabaritoAns)
    print('Respostas obtidas da prova: ', provaAns)

    # correção efetivamente sendo feita e depois um print do acerto
    acertou = getRightAnswers(gabaritoAns, provaAns)
    print('resultado final: ', acertou) # pelas minhas contas o teste deu certinho

    cv2.waitKey(0)
    cv2.destroyAllWindows()