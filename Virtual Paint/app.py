# app.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
import cv2
from color_utils import findColor
from draw_utils import drawOnCanvas

# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Webcam setup
frameWidth, frameHeight = 640, 480
cap = cv2.VideoCapture(0)  # 👈 Use 0 unless you have multiple cameras
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Define your colors
myColors = [
    [0, 186, 55, 179, 255, 255],
    [27, 137, 27, 50, 255, 255],
    [65, 60, 18, 134, 255, 255]
]
myColorValues = [
    [51, 153, 255],  # Blue
    [0, 255, 0],     # Green
    [255, 0, 0]      # Red
]

# Store points (global)
myPoints = []


def generate_frames():
    """Stream video frames after applying paint logic."""
    global myPoints
    while True:
        success, img = cap.read()
        if not success:
            break

        imgCnt = img.copy()
        newPoints = findColor(img, myColors, myColorValues, imgCnt)

        if len(newPoints) != 0:
            for p in newPoints:
                myPoints.append(p)

        if len(myPoints) != 0:
            drawOnCanvas(myPoints, myColorValues, imgCnt)

        # Convert frame to JPEG
        _, buffer = cv2.imencode('.jpg', imgCnt)
        frame = buffer.tobytes()

        # Yield frame as part of an MJPEG stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Main webpage route."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/video_feed")
def video_feed():
    """Video streaming route."""
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")
