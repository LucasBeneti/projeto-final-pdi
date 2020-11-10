import numpy as np 
import cv2
import math
from matplotlib import pyplot as plt


def splitFullImage(img):
    # divide as duas maiores colunas
    majorCols = np.hsplit(img,2)
    # cv2.imshow('primeira coluna', majorCols[0])
    # cv2.imshow('segunda coluna', majorCols[1])
    print('tamanho da primeira coluna: ', majorCols[0].shape)
    print('tamanho da segunda coluna: ', majorCols[1].shape)
    
    firstColLines = np.array_split(majorCols[0],25)
    secondColLines = np.array_split(majorCols[1],25)

    print('firstColLines: ', len(firstColLines))
    print('firstColLines type: ', firstColLines[0][0].shape)
    # cv2.imwrite('ndarraysalco.jpg', firstColLines[0])
    cv2.imshow('bla', firstColLines[0])
    # FAZER UMA FUNÇÃO PRA CROPAR E PERCORRER CADA COLUNAS
    # cv2.imshow(secondColLines[])
    # print(firstColLines[0][1])
    # for i in range(len(firstColLines)):
    #     cv2.imshow('questão 4', firstColLines[i])

        # print('tipo: ', type(firstColLines[i]))
        
    # cv2.imshow('questão 33', secondColLines[16])


