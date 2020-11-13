import numpy as np 
import cv2
import math
from matplotlib import pyplot as plt

'''
    Input:
        img - imagem de onde serão retiradas as alternativas preenchidas
    Output:
        Array cujo tamanho é o número de questões da prova (50 no nosso caso) e 
        em cada índice do vetor é a resposta para a respectiva pergunta
'''
def getFileAns(img):
    fullTestSplit = splitFullImage(img)
    nonZeroArr = getArrayOfNonZeros(fullTestSplit)
    finalAnsArr = getAnsForEachQuestion(nonZeroArr)

    return finalAnsArr

# separa a imagem completamente em 50 elementos onde cada um destes 
# é um array com 6 itens, cada item é uma imagem ou do número da questão
# ou da alternativa
def splitFullImage(processedImage):
    # divide as duas maiores colunas
    lista_questoes = [] # array de arrays que receberá cada elemento de cada questão
    majorCols = np.array_split(processedImage,2, axis=1) # split das colunas
    for col in majorCols:
        questions_img_array = np.array_split(col,25)
        for row in questions_img_array:
            curr_question =[]
            split_row = np.array_split(row,6, axis=1)
            for el in split_row:
                curr_question.append(el)

            lista_questoes.append(curr_question)
    return lista_questoes

'''
Input:
    tem como entrada um array de array com todas as questões já 
    cortadas e separadas cada uma sem seu índice corretamente

Output:
    Array de arrays onde cada elemento é o valor de pixels non zero
    referente àquele pedaço da questão
'''
def getArrayOfNonZeros(fullSplitImage):
    nonZeroValuesArray = []
    for question in fullSplitImage:
        nonZeroCount = []
        for i in range(len(question)):
            # conta não zeros e adiciona no array acima
            value = np.count_nonzero(question[i])
            nonZeroCount.append(value)
        nonZeroValuesArray.append(nonZeroCount)
    return nonZeroValuesArray

'''
    O array final com as alternativas de cada questão
    Input:
        Recebe array de arrays de valores non zero de cada quadrado da questão

    Output:
        Retorna um array com número de 0 a 5 onde 0 é anuldo, 1 é A, 2 B...
'''
def getAnsForEachQuestion(nonZeroArr):
    finalAnsForQuestion = []
    indexConverter = ['-', 'A', 'B', 'C', 'D', 'E']
    for res in nonZeroArr:
        finalAns = chooseAnswerForQuestion(res)    
            
        finalAnsForQuestion.append(indexConverter[finalAns])

    return finalAnsForQuestion
    
'''
    Potencialmente escolhe a alternativa
    Input:
        Array de valores de pixels non-zero

    Output:
        Alternativa final para aquela questão
'''
def chooseAnswerForQuestion(valuesArr):
    localAns = 0
    currMax = 0
    runnerUp = 0
    for el in valuesArr:
        if (el > currMax):
            runnerUp = currMax
            currMax = el
            localAns = valuesArr.index(el)
        elif (el > runnerUp):
            runnerUp = el1
    # variando esse coef 0.4, você determina a tolerância pra anular
    # checando se aluno marcou mais de uma resposta
    if(runnerUp >= (0.4 * currMax)):
        localAns = 0

    # checando se o aluno não marcou nenhuma resposta
    if((currMax - runnerUp) < 0.3 * currMax):
        localAns = 0

    return localAns


# imagem de enctrada tem que ser grayscale já
def getImageHist(img):
    hist = cv2.calcHist([img],[0], None,[256],[0,256])
    # plt.hist(img.ravel(),256,[0,256])
    # plt.show()