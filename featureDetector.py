import numpy as np
import cv2
from matplotlib import pyplot as plt

# # img = cv2.imread('./ImageFrames/Original/frame0.jpg',0)
# img = cv2.imread("./data_road/training/image_2/um_000000.png", 0)
#
# # Initiate FAST object with default values
# fast = cv2.FastFeatureDetector_create(threshold=30)
#
# # find and draw the keypoints
# kp = fast.detect(img,None)
# print(kp[1])
# img2 = cv2.drawKeypoints(img, kp, outImage=None, color=(255,0,0))
#
# # Print all default params
# print("Threshold: ", fast.getThreshold())
# print("nonmaxSuppression: ", fast.getNonmaxSuppression())
# print("neighborhood: ", fast.getType())
# print("Total Keypoints with nonmaxSuppression: ", len(kp))
#
# cv2.imshow('fast_true.png',img2)
#
# # Disable nonmaxSuppression
# fast.setNonmaxSuppression(0)
# kp = fast.detect(img,None)
#
# print("Total Keypoints without nonmaxSuppression: ", len(kp))
#
# img3 = cv2.drawKeypoints(img, kp, outImage=None, color=(255,0,0))
#
# # cv2.drawKeypoints(img, kp, img, )
#
# cv2.imshow('fast_false.png',img3)
# cv2.waitKey(0)

def calcDist(good_old, good_new):
    dist = []
    for i in range(good_old.shape[0]):
        delX = good_new[i, 0] - good_old[i, 0]
        delY = good_new[i, 1] - good_old[i, 1]
        dist.append(np.sqrt(np.power(delX, 2) + np.power(delY, 2)))
    return dist


def featureComparator(img1, img2):
    # params for ShiTomasi corner detection
    feature_params = dict( maxCorners = 100,
                           qualityLevel = 0.3,
                           minDistance = 7,
                           blockSize = 7 )
    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize  = (15,15),
                      maxLevel = 2,
                      criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    # Create some random colors
    color = np.random.randint(0,255,(100,3))
    # Take first frame and find corners in it
    old_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    # Create a mask image for drawing purposes
    mask = np.zeros_like(img1)
    frame_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    print(good_new.shape)
    print(good_old.shape)
    dist = []
    dist = calcDist(good_old, good_new)
    print(dist)

    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        img2 = cv2.circle(img2,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(img2,mask)
    cv2.imshow('frame',img)
    cv2.waitKey(0)

img1 = cv2.imread("./ImageFramesOld/Original/frame0.jpg")
img2 = cv2.imread("./ImageFramesOld/Original/frame1.jpg")
featureComparator(img1, img2)