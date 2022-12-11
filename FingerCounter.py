from HandDetector import HandDetector
import cv2
import mediapipe as np

video = cv2.VideoCapture(0)
detector = HandDetector()
while 1:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    detector.findHands(frame,True)
    points = detector.findPosition(frame)
    if points:
        count = 0
        if points[8][1] < points[6][1]:
            count += 1
        if points[12][1]<points[10][1]:
            count += 1
        if points[16][1]<points[14][1]:
            count += 1
        if points[20][1]<points[19][1]:
            count += 1
        if points[4][0]<points[5][0]:
            count += 1
        cv2.putText(frame, f"Count: {count}", (20, 60), cv2.FONT_HERSHEY_PLAIN, 4, 8, 3 )
    print(points)
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == 27:
        break