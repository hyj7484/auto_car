import jetson.inference
import jetson.utils
import cv2

net = jetson.inference.detectNet('ssd-mobilenet-v2', threshold = 0.5)

capture = cv2.VideoCapture(0)

while cv2.waitKey(33) < 0 :
    ret, img = capture.read()

    img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    current_time = time.time() - prev_time
    imgCuda = jetson.utils.cudaFromNumpy(img)
    detections = net.Detect(imgCuda)

    top, bottom, left, right = 0, 0, 0, 0
    for i in detections :
        print(i)
        top = int(i.Top)
        bottom = int(i.Bottom)
        left = int(i.Left)
        right = int(i.Right)
        classId = i.ClassID
        print(classId)
        className = net.GetClassDesc(classId)
        print(className)


        copyImg = img[top:bottom, left:right].copy()
        if classId == 10 :
            cv2.imshow('imgcopy', copyImg)
    img = jetson.utils.cudaToNumpy(imgCuda)
    prev_time = time.time()
    cv2.inshow('img', img)
