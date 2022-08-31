from picamera import PiCamera
import time
from imutils.video import VideoStream
import cv2

vs = VideoStream(usePiCamera=True, resolution = (900, 506)).start()
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE, 40) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 900)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 506)
time.sleep(2.0)

frame = vs.read()
cv2.imwrite("image.jpg", frame)

