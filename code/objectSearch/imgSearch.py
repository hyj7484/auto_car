import cv2
import numpy as np
import time

def color_check(img) :
    c = ['red', 'yellow', 'green']
    rs = []
    index = 2
    # Red
    rs.append(cv2.inRange(img, (0, 0, 150), (100, 100, 255)))
    # Yellow
    rs.append(cv2.inRange(img, (0, 200, 200), (100, 255, 255)))
    # green
    rs.append(cv2.inRange(img, (0, 150, 0), (100, 255, 100)))

    Max = 0
    for i in range(len(rs)) :
        value, count = np.unique(rs[i], return_counts=True)
        t = 'color' + str(i)
        cv2.imshow(t, rs[i])
        print(value)
        if 255 in value :
            value_index = np.where(value == 255)
            print(value_index, 'index ?')
            if Max < count[value_index] :
                print("??")
                Max = count[value_index]
                print(Max)
                index = i
    if Max <= 0 :
        return "none"
    text = 'color img' + str(count)
    print(index)
    cv2.imshow(text, img)
    cv2.imshow(c[index], rs[index])
    return c[index]


weights="./yolo/yolov2-tiny.weights"
cfg="./yolo/yolov2-tiny.cfg"
coco="./yolo/coco.names"

net = cv2.dnn.readNet(weights, cfg)
classes = []
with open(coco, "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in [net.getUnconnectedOutLayers()]]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

def searchImg(img) :
    # img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # traffic light number = 9
            # class_id == 9  = traffic light

            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    count = 0

    copyImg = img.copy()
    # view prt text and lines
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            if label == 'traffic light' :
                copy = copyImg[y:y+h+h, x:x+w]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 4)
            count+=1
            text = label + str(count)
            cv2.putText(img, text, (x, y + 30), font, 2, color, 2)
    cv2.imshow('img', img)

if __name__ == "__main__" :
    video = cv2.VideoCapture(0)
    prev_time = 0
    FPS = 3
    while cv2.waitKey(33) < 0 :
        ret, frame = video.read()
        current_time = time.time() - prev_time
        if ret and current_time > 1. / FPS :
            prev_time = time.time()
            searchImg(frame)
