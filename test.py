# import numpy
import cv2

img = cv2.imread("./images/gabarito.jpeg",0) # 0 seta a leitura para grayscale
img_medianblur = cv2.medianBlur(img,5)
th1 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,7)
th2 = cv2.adaptiveThreshold(img_medianblur,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,7)
# canny_output = cv2.Canny(img, 120,50)

cv2.imshow('Original',img)
cv2.imshow('Thresh Adaptativo Gaussiano sem blur com constante 7',th1)
cv2.imshow('Thresh Adaptativo Medio sem blur com constante 7',th2)
# cv2.imshow('Canny Output',canny_output)
output = th2.copy()
countours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(countours)):
    cv2.drawContours(output, countours, i, (0,255,0),3)

cv2.imshow('imagem com contornos', output)

# morph open na output

# morph close na output

# fill ?

cv2.waitKey()
cv2.destroyAllWindows()

# instalar com -r <nome da file>
# converter imagme pra cinza
# - passar um blur 3x3