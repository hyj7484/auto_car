import cv2
import time

cap = cv2.VideoCapture(0)

count = 0

prev_time = 0
FPS = 5
while cv2.waitKey(33) < 0 :
    ret, img = cap.read()

    curTime = time.time() - prev_time
    if ret and curTime > 1. /FPS :
        prev_time = time.time()
        text = './ImgCapture/capture_' + str(count) + '.jpg'
        cv2.imwrite(text, img)
        count += 1
    cv2.imshow('img', img)
