import numpy as np
import cv2
import sys
import os
import matplotlib.pyplot as plt

def storeFrames(videoFile):
    vidCap = cv2.VideoCapture(videoFile)
    success, image = vidCap.read()
    count = 0
    while success:
        success, image = vidCap.read()
        try:
            frame = resizeImg(image)
            frame = cv2.resize(frame,(640, 640))
            cv2.imwrite("./ImageFrames/Original/frame%d.jpg" % count, frame)
        except:
            continue

          # save frame as JPEG file
        if cv2.waitKey(10) == 27:  # exit if Escape is hit
            break
        count += 1
    return count


def processImage(imgName):
    img = cv2.imread(imgName)
    height, width, channels = img.shape
    imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(imgGrayScale, 180, 255, cv2.THRESH_BINARY)

    pHeight = 2 * height // 3
    pWidth = 150
    imgSize = 600

    # pts1 = np.float32([[pWidth, pHeight], [width - pWidth, pHeight], [0, height], [width, height]])
    pts1 = np.float32([[171,338], [513,328], [19,401], [513, 409]])
    pts2 = np.float32([[0, 0], [imgSize, 0], [0, imgSize], [imgSize, imgSize]])

    transform = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(thresh1, transform, (imgSize,imgSize))

    return dst


def resizeImg(img):
    height, width, _ = img.shape
    frame = img[0:height//2, width//2:width]
    return frame


def reduceIntensity(height, width, img):
    ht, wt = img.shape
    for i in range(height + 1, ht):
        img[i, width] = 0
    return img


def imageEdges(imgName):
    img = cv2.imread(imgName)
    height, width, channels = img.shape
    imgGrayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(imgGrayScale, 180, 255, cv2.THRESH_BINARY)

    for i in range(width):
        for j in range(height):
            if thresh1[j, i] > 0:
                continue
            else:
                thresh1 = reduceIntensity(j, i, thresh1)
                break
    return thresh1


if __name__ == '__main__':
    # videoFile = sys.argv[1]
    # if not os.path.exists("./ImageFrames/Original/"):
    #     os.makedirs("./ImageFrames/Original/")
    # if not os.path.exists("./ImageFrames/Edges/"):
    #     os.makedirs("./ImageFrames/Edges/")
    # if not os.path.exists("./ImageFrames/TopDown/"):
    #     os.makedirs("./ImageFrames/TopDown/")
    # count = storeFrames(videoFile)
    # trans = []
    # mod = []

    # dat_files = [f for f in os.listdir("./data_road/training/image_2/") if f.endswith('.png')]
    # for file in dat_files:
    #     img = cv2.imread("./data_road/training/image_2/" + file)
    #     cv2.imshow("Org", img)
    #     cv2.imshow("new", imageEdges("./data_road/training/image_2/" + file))
    #     cv2.waitKey(0)

    # for i in range(count):
    #
    #     imgName = "./data_road/training/image_2/um_000000"
    #     imgName = "./ImageFrames/Original/frame" + str(i) + ".jpg"
    #     trans.append(processImage(imgName))
    #     mod.append(imageEdges(imgName))
    #
    # height, width = trans[0].shape
    #
    # # transVideo = cv2.VideoWriter("./ImageFrames/TopDown/birdsEyeView.mp4", 0x00000021, 30, (width, height))
    # edgeVideo = cv2.VideoWriter("./ImageFrames/Edges/edges.mp4", 0x00000021, 30, (width, height))
    #
    # for i in range(count):
    #     cv2.imwrite("./ImageFrames/TopDown/topDown%d.jpg" % i, trans[i])
    #     cv2.imwrite("./ImageFrames/Edges/mod%d.jpg" % i, mod[i])
    #     # transVideo.write(trans[i])
    #     edgeVideo.write(mod[i])
    # # transVideo.release(
    # edgeVideo.release()
    img = cv2.imread("./ImageFramesOld/TopDown/topDown275.jpg", 0)
    height, width = img.shape
    ret, img = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
    cv2.imshow("new", img)
    cv2.waitKey(0)

    d = []
    idx = []

    print(height // 50)
    for i in range(height // 50):
        plt.cla()
        d = []
        idx = []
        for j in range(width):
            d.append(img[50 * i, j])
            idx.append(j)
        plt.plot(idx, d)
        print(d)
        plt.show()




    # print(d)
    # for i in range(len(d) - 1):
    #     if d[i] - d[i+1] < 30:
    #         d[i]=0
    #     else:
    #         d[i] = 100
    #
    # plt.plot(idx, d)
    # plt.show()
