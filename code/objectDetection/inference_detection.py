import jetson.inference as inference
import jetson.utils as utils
import cv2
import numpy as np
import time as t

net = None

def init(model='ssd-mobilenet-v2'):
    global net
    net = inference.detectNet(model, threshold = 0.5)

def getDetections(img) :
    # img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    cuda = utils.cudaFromNumpy(img)
    detections = net.Detect(cuda)
    detectImg = utils.cudaToNumpy(cuda)
    return detections, detectImg

# --model=models/test/ssd-mobilenet.onnx', '--labels=models/test/labels.txt', '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes'
