import cv2
import numpy as np

# capture
# gray color
# blur ( 노이즈 제거 )
# HSV기반 2진화 방법

def setGrayColor(img) :
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def setBlur(img) :
    gray = setGrayColor(img)
    return cv2.GaussianBlur(gray, (5, 5), 0)

def setHSV(img, array1=[0,0,200], array2=[131,255,255]) :
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_white = np.array(array1)
    upper_white = np.array(array2)
    cv2.imshow('hsv', hsv)
    # print(lower_white)
    # print(upper_white)
    return cv2.inRange(hsv, lower_white, upper_white)

def setCanny(img) :
    blur = setBlur(img)
    return cv2.Canny(blur, 20, 190)

def nonZero(img, startX=0, endX=640, draw_height=430, draw_height_size=20, draw_width_size=20):
    # startX = 시작 x지점
    # endX = 끝 x지점
    # draw_height = y 지점
    # draw_height_size = 높이 값
    # draw_width_size = 가로

    # get HSV
    hsv = setHSV(img)
    cv2.imshow('imgss', hsv)
    height, width = img.shape[:2]
    if draw_height + draw_height_size > height :
        draw_height = height - draw_height_size

    if endX > width :
        endX = width
    count = 0
    whiteList = []
    while True :
        count+=1
        area = hsv[draw_height:draw_height+draw_height_size, startX:startX+draw_width_size-2]

        if cv2.countNonZero(area) > 160 :
            cv2.rectangle(img,(startX, draw_height), (startX+draw_width_size-2, draw_height+draw_height_size), (0,255,0), 2)
            whiteList.append(startX)
        else :
            cv2.rectangle(img,(startX, draw_height), (startX+draw_width_size-2, draw_height+draw_height_size), (255,0,0), 2)
        startX = startX+draw_width_size
        if startX + draw_width_size - 2 > endX:
            break
    return img, whiteList

cap = cv2.VideoCapture('./video/track/2.mp4')
while cv2.waitKey(33) < 0 :
    ret, img = cap.read()
    if not ret :
        break

    firstList = []
    secondList = []
    img, firstList = nonZero(img, draw_height=900, endX=img.shape[1]-20)
    img, secondList = nonZero(img, draw_height=850, startX=50, endX=img.shape[1]-100)

    cv2.imshow('non', img)
