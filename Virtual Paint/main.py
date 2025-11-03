import cv2
from color_utils import findColor
from draw_utils import drawOnCanvas

frameWidth, frameHeight = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [
    [0, 186, 55, 179, 255, 255],
    [27, 137, 27, 50, 255, 255],
    [65, 60, 18, 134, 255, 255]
]
myColorValues = [
    [51, 153, 255],  # blue
    [0, 255, 0],  # green
    [255, 0, 0]  # red
]
myPoints = []

while True:
    success, img = cap.read()
    imgCnt = img.copy()
    newPoints = findColor(img, myColors, myColorValues, imgCnt)

    if len(newPoints) != 0:
        for p in newPoints:
            myPoints.append(p)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues, imgCnt)

    cv2.imshow("Virtual Paint", imgCnt)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
