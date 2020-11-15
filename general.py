import cv2
import numpy as np

# não saquei o motivo do resize
def getResizedImage(img):
    maxHeight = 800
    height, width, channels = img.shape
    ratio = width / height
    if height > maxHeight:
        newWidth = maxHeight * ratio
        return cv2.resize(img, (int(newWidth), int(maxHeight)))
    return img

def getPreProcessedImage(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 10, 50)
    return imgCanny

# teremos que explicar como é feito essa aquisição do contorno
def getContourWithBiggestArea(image):
    contours, hierarchy = cv2.findContours(
        image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    area = 0
    contour = None

    for c in contours:
        a = cv2.contourArea(c)
        if a > area:
            area = a
            contour = c

    return contour

def getOrderedRectFromContour(contour):
    rect = np.zeros((4, 2), dtype="float32")
    perimeter = cv2.arcLength(contour, True)
    points = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    points = np.reshape(points, (4, 2))

    sum_ = points.sum(axis=1)
    diff = np.diff(points, axis=1)

    rect[0] = points[np.argmin(sum_)]  # top-left
    rect[1] = points[np.argmin(diff)]  # top-right
    rect[2] = points[np.argmax(sum_)]  # bottom-right
    rect[3] = points[np.argmax(diff)]  # bottom-left

    return rect

def getWarpedImageFromContour(image, contour):
    rect = getOrderedRectFromContour(contour)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    widthB = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    heightB = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    maxHeight = max(int(heightA), int(heightB))

    destination = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    perspective = cv2.getPerspectiveTransform(rect, destination)
    warped = cv2.warpPerspective(image, perspective, (maxWidth, maxHeight))

    return warped

def getImageWithThreshold(img):
    # valor do threshold é 85 por ser baixo e separar bem as marcações
    # das alternativas não marcadas (número de pixels não 0 ficam mais discrepantes)
    return cv2.threshold(img, 85, 255, cv2.THRESH_BINARY_INV)[1]

# aqui dá pra botar o np.arrau_split pra fazer a divisão das células
def getAnswersFromProcessedImage(img, threshold):
    height, width, channels = img.shape

    height = int(height)
    width = int(width)
    halfWidth = int(width / 2)

    cellWidth = int(halfWidth / 6)
    cellHeight = int(height / 25)
    cellSize = cellWidth * cellHeight

    left = img[0:height, cellWidth:(halfWidth)]

    out = np.concatenate((
        img[0:height, cellWidth:(halfWidth)],
        img[0:height, (halfWidth + cellWidth):width]
    ), axis=0)

    options = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

    answers = [None] * 50

    cv2.imshow("Out", out)
    

    # não chega fazer um array novo com as imagens divididas, só mexe com
    # as posições obtidas anteriormente
    for row in range(0, 50):
        y = row * cellHeight
        rowAnswers = [None] * 5
        for coll in range(0, 5):
            x = coll * cellWidth
            cell = out[y:y+cellHeight, x:x+cellWidth]
            rowAnswers[coll] = np.count_nonzero(cell)
        answered = [(item / cellSize) > threshold for item in rowAnswers]
        if sum(answered) == 1:
            answers[row] = options[answered.index(True)]

    return answers

def getAnswersFromTest(img):
    # img = cv2.imread(os.path.abspath(path))
    img = getResizedImage(img)
    imgPre = getPreProcessedImage(img)
    contour = getContourWithBiggestArea(imgPre)
    imgThreshold = getImageWithThreshold(img)
    imgWarped = getWarpedImageFromContour(imgThreshold, contour)
    return getAnswersFromProcessedImage(imgWarped, 0.55)