import cv2
import numpy
from matplotlib import pyplot as plt

gabarito = cv2.imread('./images/gabarito.jpeg')
gabarito_1 = cv2.imread('./images/gabarito_1.jpeg')
gabarito = cv2.cvtColor(gabarito, cv2.COLOR_BGR2GRAY)
gabarito_1 = cv2.cvtColor(gabarito_1, cv2.COLOR_BGR2GRAY)

# thresholding na mão
# se a imagem tem muita sombra, o thresh igual pra todas, fica ruim fica uma bosta
thresh_val = 60
thresh_gabarito = cv2.threshold(gabarito, thresh_val, 255, cv2.THRESH_BINARY_INV)[1]
# otsu se perde por causa da sombra, teria que ser um adaptativo
thresh_gabarito_1 = cv2.threshold(gabarito_1, thresh_val, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

gauss_blur = cv2.GaussianBlur(gabarito_1, (5,5),0)
adptv_thersh = cv2.adaptiveThreshold(gauss_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

# pegar historgrama (da imagem não invertida) e analizar a quantidade de preto que ela tem
hist_gabarito = cv2.calcHist([gabarito],[0],None,[256],[0,256])
hist_gabarito_1 = cv2.calcHist([gabarito_1],[0],None,[256],[0,256])
# plt.plot(hist_gabarito)
# plt.plot(hist_gabarito_1)
# plt.show()
print(type(hist_gabarito))

cv2.imshow('gabarito', gabarito)
cv2.imshow('gabarito_1', gabarito_1)
cv2.imshow('thresh_gabarito', thresh_gabarito)
cv2.imshow('thresh_gabarito_1', thresh_gabarito_1)

cv2.imshow('adaptativo', adptv_thersh)

# cv2.imwrite('gabarito_sombra.png', thresh_gabarito_1)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Para limiarização não teve jeito, tivemos que utilizar o mais basico (threshhold com valor meio fixo),
# tinha que ser algum valor consideravelmente baixo (cinza mais perto do preto do que branco) e por isso
# não podemos aceitar imagens com muita sombra.

# Testes feitos:
# [X] - adaptativo com gaussiano
# [X] - adaptativo calculando média
# [X] - passando alguns tipos de blur antes de tentar thresholding (blur padrão que é basicamente uma
#       operação com a média e blur gaussiano)