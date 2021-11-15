import cv2

import lidar.lidar as lidar
import objectSearch.imgSearch as imgS
import csiCam

if __name__ == "__main__" :
    # lidar
    ret = laser.initialize()
    if ret :
        ret = lidar.laser.turnOn()
        scan = lidar.ydlidar.LaserScan()
    # video capture
    capture = csiCam.show_camera()
    while cv2.waitKey(33) < 0 :
        # lidar
        if ret and ydlidar.os_isOk() :
            angle, range = lidar.playLidar_While(scan)
        # obejct Search
        ret1, frame = capture.read()
        if ret1 :
            imgS.searchImg(frame, weights='./yolo/yolov2-tiny.weights', cfg='./yolo/yolov2-tiny.cfg', coco='./yolo/coco.names')
