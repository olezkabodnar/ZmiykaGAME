from HandDetector import HandDetector
import cv2
import os
import numpy as np

fileNames = os.listdir("design")
imageList = []
for fileName in fileNames:
    image = cv2.imread(f"design/{fileName}")
    imageList.append(image)
header = imageList[0]
video = cv2.VideoCapture(0)
detector = HandDetector()
color = (0,0,255)
back = np.zeros((800, 1200, 3),np.uint8)

while 1:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame,(1280,800))
    frame = detector.findHands(frame)
    pointList = detector.findPosition(frame)
    if pointList:
        x, y = pointList[0]
        print(pointList[0])
        if x > 320 and x < 380 and y < 750 and y > 620:
            color = (0,0,255)
            header = imageList[0]
        if x < 690 and x > 620 and y < 750 and y > 620:
            color = (255, 0, 0)
            header = imageList[1]
        if x > 960 and x < 1020 and y < 750 and y > 620:
            color = (0, 255, 0)
            header = imageList[2]
        if x > 1050 and x < 1120 and y < 660 and y > 620:
            color = (255, 255, 255)
            header = imageList[3]
        cv2.circle(back, pointList[8],15, color, -1)
        cv2.circle(frame, pointList[8],15, color, -1)


    frame[660:800, 0:1280] = cv2.resize(header,(1280,140))
    a, imgFinal = cv2.threshold(back, 38, 255, cv2.THRESH_BINARY_INV)
    frame = cv2.bitwise_and(frame, imgFinal)
    cv2.imshow("image", cv2.bitwise_or(frame, back))
    if cv2.waitKey(1) == 27:
        break