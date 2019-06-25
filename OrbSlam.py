import cv2

def readVideo(video):
    vid = cv2.VideoCapture(video)

    if (vid.isOpened() == False):
        print("error")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret == True:
            frame = cv2.resize(frame, (640, 480))
            frame = features(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    vid.release()
    cv2.destroyAllWindows()

def features(frame):
    orb = cv2.ORB_create(1000)
    kp, des = orb.detectAndCompute(frame, None)
    cv2.drawKeypoints(frame, kp, frame,  color=(0,255,0), flags=0)
    return frame

readVideo('Car.mp4')