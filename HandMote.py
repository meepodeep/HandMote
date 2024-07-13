import numpy as np
import cv2
import mediapipe as mp
import time 
import pyautogui as pag
cx = 0
cy = 0
pag.FAILSAFE = False
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:

    ret, frame = cap.read()

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (1920, 1080))
    results = hands.process(imgRGB)
    cxInverse = (cx *-1) + 1920
    if results.multi_hand_landmarks:
        pag.moveTo(2.2*cxInverse, 2*cy,.01)
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id,lm)
                if id == 0:
                    cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

        

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



