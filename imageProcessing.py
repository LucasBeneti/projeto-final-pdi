import cv2

def preprocessImages(img, threshold):
        # blur = cv2.GaussianBlur(img,(5,5),0)
    threshImg = cv2.threshold(img, threshold,255,cv2.THRESH_BINARY_INV)[1]

    return threshImg


