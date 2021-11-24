import os
import ydlidar
import time
import sys

# YDLidar Set
ydlidar.os_init()
ports = ydlidar.lidarPortList()
port = '/dev/ydlidar'
for key, value in ports.items() :
    port = value
laser = ydlidar.CYdLidar()
laser.setlidaropt(ydlidar.LidarPropSerialPort, port);
laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 128000);
laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TOF);
laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL);
laser.setlidaropt(ydlidar.LidarPropScanFrequency, 10.0);
laser.setlidaropt(ydlidar.LidarPropSampleRate, 20);
laser.setlidaropt(ydlidar.LidarPropSingleChannel, False);

def playLidar_start() :
    ret = laser.initialize()
    if ret :
        ret = laser.turnOn()
        scan = ydlidar.LaserScan()
        while ret and ydlidar.os_isOk() :
            angle, range = playLidar(scan)


def playLidar(scan) :
    ang = []
    ran = []
    r = laser.doProcessSimple(scan)
    if r :
        for point in scan.points :
            if point.angle < -2.5 or point.angle > 2.5 :
                ang.append(point.angle)
                ran.append(point.range)
    else :
        print('Failed to get Lidar Data')
    return ang, ran

if __name__ == "__main__" :
    playLidar_start()
