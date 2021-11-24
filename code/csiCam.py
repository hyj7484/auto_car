# jetson camera
import cv2

def gstreamer_pipeline(
    capture_width=640,
    capture_height=480,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            capture_width,
            capture_height,
        )
    )


def show_camera(width=640, height=480):
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=2, capture_width=width, capture_height=height), cv2.CAP_GSTREAMER)
    if cap.isOpened():
        cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        if __name__ != 'main' :
            return cap
        while cv2.waitKey(33) < 0 :
            ret, frame = cap.read()
            if not ret :
                break
            cv2.imshow('frame', frame)
        # Window
    else:
        print("Unable to open camera")

if __name__ == '__main__' :
    show_camera()
