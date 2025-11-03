# 🎨 Virtual Paint

## 🧠 Project Overview  
Virtual Paint is an interactive computer vision project that allows users to draw in real time using colors and a webcam feed.  
By detecting colored objects (for example a colored marker or cap) and using their positions in the camera frame, the app draws on the screen — giving a “paint in air” effect.

The project uses:  
- **OpenCV** for color detection and contour tracking  
- **HSV color space** for robust color segmentation  
- A live video feed from a webcam  
- Optionally, **FastAPI** for streaming the output to a web page (if deployed)  

---

## 🛠️ Features  
- Detects multiple predefined colors (configured via HSV ranges).  
- Tracks the position of the detected color and draws on the canvas accordingly.  
- Keeps the drawn points persistent until cleared (you can extend this).  
- Modular code structure: `color_utils.py`, `draw_utils.py`, `main.py` (and `app.py` for web version).  
- Easy to extend: add more colors, clear canvas button, upload image/video mode, etc.

---

## 📂 Project Structure  
Virtual Paint/
├── app.py # FastAPI server (optional web deployment)
├── main.py # Core application logic (OpenCV loop)
├── color_utils.py # Color detection & contour utilities
├── draw_utils.py # Drawing functions
├── templates/
│ └── index.html # Web UI page (for FastAPI version)
├── requirements.txt # Python dependencies
└── Resources/ # (optional) Images or sample media

