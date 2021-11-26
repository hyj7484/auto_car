import cv2
import numpy as np

def colorSearch(img) :
    imgList = []
    colors = ['red', 'yellow', 'green']
    colorIndex = 3

    # Red
    imgList.append(cv2.inRange(img, (0, 0, 200), (100, 100, 255)))
    # Yellow
    imgList.append(cv2.inRange(img, (0, 200, 200), (100, 255, 220)))
    # green
    # imgList.append(cv2.inRange(img, (0, 150, 0), (100, 255, 100)))
    imgList.append(cv2.inRange(img, (100, 200, 0), (160, 255, 124)))
    # white
    # white = cv2.inRange(img, (240, 240, 240), (255, 255, 255))
    # if not 255 in white :
    #     return 'none'
    # whereWhite = np.where(white == 255)
    # # sortWhite = np.sort(whereWhite[1])
    # #
    # # print(len(sortWhite))
    # # print(sortWhite)
    # avg = ( max(whereWhite[1]) + min(whereWhite[1])) / 2
    # # cv2.imshow('g',imgList[2])
    # # cv2.imshow('w', white)

    for index, i in enumerate(imgList) :
        if not 255 in i :
            continue
        value, count = np.unique(i, return_counts=True)
        countChk = np.where(value==255)
        if count[countChk] < 500 :
            continue
        # value, count = np.unique(i, return_counts=True)
        # whereWhite = np.where(value == 255)
        # if count[whereWhite] < 50 :
        #     continue


        where = np.where(i == 255)
        maxY = max(where[0])
        minY = min(where[0])
        maxX = max(where[1])
        minX = min(where[1])
        maxY = maxY if maxY > minY else minY+1
        maxX = maxX if maxX > minX else minX + 1
        # print(img.shape)
        # print(minY, maxY)
        # print(minX, maxX)
        # print('min, max')
        copyImg = img[minY:maxY, minX:maxX].copy()
        # cv2.imshow('s',copyImg)
        white = cv2.inRange(copyImg, (220, 220, 220), (255, 255, 255))
        # w = np.where(white == 255)
        value, count = np.unique(white, return_counts=True)
        # print(value)
        # print(count)
        cv2.imshow('s', copyImg)
        if 255 in white :
            # print(w)
            cv2.imshow('white', white)
            colorIndex = index

    #     if mi < avg < ma :
    #         colorIndex = index
    if colorIndex >= len(colors) :
        print('none 3')
        return img
    #
    print(colorIndex)
    cv2.imshow(colors[colorIndex], imgList[colorIndex])
    print(colors[colorIndex])

    where = np.where(imgList[colorIndex] == 255)
    h = max(where[0])
    y = min(where[0])
    w = max(where[1])
    x = min(where[1])
    color = [200, 200, 100]
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.rectangle(img, (x, y), (w, h), color, 4)
    cv2.putText(img, colors[colorIndex], (x, y + 30), font, 2, color, 2)
    return img
    #
    # # bgr
    # height, width, chanel = img.shape
    # width = width / 5
    # white = cv2.inRange(img, (240, 240, 240), (255, 255, 255))
    # v, c = np.unique(white, return_counts=True)
    # whiteIndex = np.where(v == 255) if 255 in v else False
    # MaxW = 0
    # MinW = 0
    # if whiteIndex and c[whiteIndex] > 50 :
    #     white_where = np.where(white == 255)
    #     MaxW = max(white_where[1])
    #     MinW = min(white_where[1])
    # Max = 0
    # cv2.imshow('white', white)
    #
    # almost = 99999
    #
    # for index, i in enumerate(imgList) :
    #     value, count = np.unique(i, return_counts=True)
    #     if index == 2 :
    #         print(count)
    #     # print(count)
    #     x = np.where(value == 255)
    #     if 255 in i and MaxW != 0 and count[x] > 1000:
    #         where = np.where(i == 255)
    #         maxI = abs(MaxW - max(where[1]))
    #         minI = abs(MinW - min(where[1]))
    #         cal = maxI if maxI < minI else minI
    #         if almost > cal:
    #             almost = cal
    #             colorIndex = index
    #
    # # if colorIndex == 1 :
    # #     value, count = np.unique(imgList[colorIndex], return_counts=True)
    # #     print(value, count)
    #     # if 255 in value :
    #     #     value_index = np.where(value == 255)
    #     #     print(count[value_index], colors[index])
    #     #     if Max < count[value_index] and count[value_index] > 20:
    #     #         Max = count[value_index]
    #     #         colorIndex = index
    #             # print(Max)
    #
    # if colorIndex < 3 :
    #     cv2.imshow(colors[colorIndex], imgList[colorIndex])
    #     print(colors[colorIndex])

if __name__ == "__main__" :
    cap = cv2.VideoCapture('./video/light2.mp4')
    while cv2.waitKey(33) < 0 :
        ret, frame = cap.read()
        frame = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_AREA)
        # frame = frame[300:700, 800:1300].copy()
        if not ret :
            break
        # frame = frame[200:300, 100:200]
        frame = colorSearch(frame)
        # cv2.putText(img, text, (x, y + 30), font, 2, color, 2)
        cv2.imshow('frame', frame)
    pass
