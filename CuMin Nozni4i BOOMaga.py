from HandDetector import HandDetector
import cv2
video = cv2.VideoCapture(0)
detector = HandDetector()
while 1:
    ret, frame = video.read()

    frame = cv2.flip(frame, 1)
    detector.findHands(frame, True)
    points = detector.findPosition(frame)
    if points:
        game = ""
        if  points[8][1] and points[12][1] < points[9][1]:
            game = "nozni4i"
        if points[16][1] and points[20][1]  <  points[10][1] and points[13][1]:
            game = "bymaga"
        if points[8][1] and points[12][1] > points[5][1]:
            game = "kamin"

        cv2.putText(frame, f": {game}", (20, 60), cv2.FONT_HERSHEY_PLAIN, 4, 8, 3 )
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) == 27:
        break