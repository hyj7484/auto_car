import cv2
import numpy as np

import lidar.lidar as lidar
import objectDetection.inference_detection as detection
import csiCam as csi

if __name__ == "__main__" :
    # lidar
    ret = lidar.laser.initialize()
    if ret :
        ret = lidar.laser.turnOn()
        scan = lidar.ydlidar.LaserScan()

    # camera
    detection.init()
    cap = csi.show_camera()

    angle, range = [], []
    while cv2.waitKey(33) < 0 :
        if ret and lidar.ydlidar.os_isOk() :
            angle, range = lidar.playLidar(scan)
        ret_cap, img = cap.read()
        detection, detectImg = detection.getDetections(img)
        cv2.imshow('img', detectImg)
