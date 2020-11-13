import cv2
import numpy as np

warp_test = cv2.imread('./images/warp_fundo_ver1.jpeg')

warp_test = cv2.cvtColor(warp_test, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(warp_test,(5,5),1)
imgCanny = cv2.Canny(imgBlur, 10,50)

imgContours = warp_test.copy()

contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour_areas = []
for i in range(len(contours)):
    contour_areas.append(cv2.contourArea(contours[i]))

print(contour_areas)





max_area_idx = 0
max_area_val = 0
for i in range(len(contours)):
    # print('tamanho do contorno: ', len(contour))
    
    if(cv2.contourArea(contours[i]) > max_area_val):
        # print('maior: ', cv2.contourArea(contours[i]))
        max_area_idx = i
        max_area_val = cv2.contourArea(contours[i])
    


rect = cv2.minAreaRect(contours[0])
box_points = cv2.boxPoints(rect)
box_points = np.int0(box_points)
cv2.drawContours(imgContours, [box_points], 0, (255,0,0),2)
print(rect)
print(max_area_idx)
print(max_area_val)

cv2.imshow('warp original', warp_test)
cv2.imshow('warp canny', imgCanny)
cv2.imshow('contours', imgContours)

# cv2.imwrite('contornos.jpeg',imgContours)

cv2.waitKey()
cv2.destroyAllWindows()