from HandDetector import HandDetector
import cv2
import pyautogui as pag

print(pag.size())

pag.moveTo
video = cv2.VideoCapture(0)
detector = HandDetector()
while 1:
    ret, frame = video.read()

    frame = cv2.flip(frame, 1)
    detector.findHands(frame, True)
    points = detector.findPosition(frame)
    if points:
        x = (points[16][0] * 1920/640)
        y = (points[16][1] * 1080/400)
        if points[8][1] > points[7][1]:
            pag.click()
        if points[12][1]>points[11][1]:
            pag.click(button="right")
        pag.moveTo(x, y)

        print(points[16])
    #cv2.imshow("Image", frame)
    if cv2.waitKey(1) == 27:
        break