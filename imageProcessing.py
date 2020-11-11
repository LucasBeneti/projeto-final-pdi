import cv2

def preprocessImages(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret, threshImg = cv2.threshold(blur, 0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    return threshImg


