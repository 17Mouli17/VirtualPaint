import cv2
import numpy as np

def getContours(image):
    contours, hirerachy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def findColor(image, colors, color_values, imgCnt):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    newPoints = []
    for i, col in enumerate(colors):
        lower, upper = np.array(col[0:3]), np.array(col[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgCnt, (x, y), 10, color_values[i], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, i])
    return newPoints

