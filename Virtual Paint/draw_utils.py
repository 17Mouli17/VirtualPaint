import cv2

def drawOnCanvas(points, color_values, imgCnt):
    for point in points:
        cv2.circle(imgCnt, (point[0], point[1]), 10, color_values[point[2]], cv2.FILLED)
