import cv2


cap = cv2.VideoCapture(0)

while cv2.waitKey(33) < 0 :
    ret, img = cap.read()
    img = cv2.resize(img, (640, 480))
    cv2.imshow('img', img)
