import numpy as np
import cv2

img = cv2.imread("./images/gabarito.jpeg",0) # 0 seta a leitura para grayscale
img_medianblur = cv2.medianBlur(img,5)
th1 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,7)
th2 = cv2.adaptiveThreshold(img_medianblur,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,7)
# canny_output = cv2.Canny(img, 120,50)

# cv2.imshow('Original',img)
# cv2.imshow('Thresh Adaptativo Gaussiano sem blur com constante 7',th1)
# cv2.imshow('Thresh Adaptativo Medio sem blur com constante 7',th2)
# cv2.imshow('Canny Output',canny_output)
print('tamanho da imagem', th1.shape)
output = np.zeros([th1.shape[0], th1.shape[1],1], np.uint8)
output.fill(255)

output_2 = np.zeros([th1.shape[0], th1.shape[1],1], np.uint8)
output_2.fill(255)
countours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(countours)):
    cv2.drawContours(output, countours, i, (0,255,0),3)

cv2.imshow('imagem com todos os contornos', output)


countour_number = 0
for i in range(len(countours)):
    isConvex = cv2.isContourConvex(countours[i])
    if(isConvex == True and cv2.contourArea(countours[i]) > 130):
            countour = countours[i]
            countour_number +=1
            cv2.drawContours(output_2, countour, -1, (0,255,0),3)

print("numero de countours encontrados: ", countour_number)
        
cv2.imshow("output_2", output_2)

# cv2.imshow('imagem com contornos', output)
# kernel = np.ones((3,3), np.uint8)
# morph open na output
# erosion = cv2.erode(output, kernel, iterations=5)
# cv2.imshow('erosao da imagem', erosion)
# morph close na output

# fill ?

cv2.waitKey()
cv2.destroyAllWindows()

# instalar com -r <nome da file>
# converter imagme pra cinza
# - passar um blur 3x3