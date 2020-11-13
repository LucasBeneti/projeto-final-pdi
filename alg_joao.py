import cv2
import numpy as np

def findBoundsContour(image):
    area = 0
    contour = None

    for c in contours:
        a = cv2.contourArea(c)
        if a > area:
            area = a
            contour = c

    return contour

def getOrderedRectFromContour(contour):
    rect = np.zeros((4, 2), dtype = "float32")
    perimeter = cv2.arcLength(contour, True)
    points = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    points = np.reshape(points, (4, 2))

    sum_ = points.sum(axis = 1)
    diff = np.diff(points, axis = 1)

    rect[0] = points[np.argmin(sum_)] # top-left
    rect[1] = points[np.argmin(diff)] # top-right
    rect[2] = points[np.argmax(sum_)] # bottom-right
    rect[3] = points[np.argmax(diff)] # bottom-left

    return rect

def warpAndCropContour(image, contour):
    rect = getOrderedRectFromContour(contour)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    widthB = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    heightB = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    maxHeight = max(int(heightA), int(heightB))

    destination = np.array([
        [0,0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    perspective = cv2.getPerspectiveTransform(rect, destination)
    warped = cv2.warpPerspective(image, perspective, (maxWidth, maxHeight))

    return warped

img = cv2.imread("./images/warp_fundo_ver2.jpeg")
# img = cv2.resize(img, (500, 500))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
imgCanny = cv2.Canny(imgBlur, 10, 50)

contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour = findBoundsContour(contours)

w = warpAndCropContour(img, contour)
w = cv2.cvtColor(w, cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(w, 120,255,cv2.THRESH_BINARY_INV)[1]
cv2.imwrite('warp_joao.png', threshImg)
cv2.imshow("Output", threshImg)

cv2.waitKey(0)