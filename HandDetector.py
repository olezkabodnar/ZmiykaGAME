import cv2
import mediapipe as mp

mpHands = mp.solutions.hands

class HandDetector:
    def __init__(self, mode = False, maxHands=2):
        self.hands = mpHands.Hands(mode, maxHands)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,img, draw=True):
        self.results = self.hands.process(img)
        self.data = self.results.multi_hand_landmarks
        if draw and self.data:
            for hand in self.data:
                self.mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self, img, hand=0):
        pointList = []
        if self.data:
            for landmark in self.data[hand].landmark:
                h, w = img.shape[:2]
                x, y = int(w*landmark.x), int(h*landmark.y)
                pointList.append((x,y))
        return pointList

if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    detector = HandDetector()
    while 1:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        detector.findHands(frame,True)
        points = detector.findPosition(frame)
        print(points)
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) == 27:
            break