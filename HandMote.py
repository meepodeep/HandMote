import numpy as np
import cv2
import mediapipe as mp
import time 
import pyautogui as pag
import multiprocessing



cx = 0
cxInverse = 0
cy = 0
pag.FAILSAFE = False
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
    
def MoveMouse(cxInverse, cy):
    pag.moveTo(cxInverse, cy,.2)

def TrackHand(frame, hands, mpDraw, mpHands):
    
    cxInverse = (cx *-1) + 1920
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (1920, 1080))
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 5:
                    cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow('frame', frame)
    


    while True:
        if __name__ == "__main__":
            
            ret, frame = cap.read()

            
            p1 = multiprocessing.Process(target=TrackHand, args=(ret, frame, hands, mpDraw, mpHands))
            p2 = multiprocessing.Process(target=MoveMouse, args=(cxInverse,cy))

            p1.start()
            p2.start()

            p1.join()
            p2.join()
            
            if cv2.waitKey(1) == ord('q'):
                break
            cv2.destroyAllWindows()
            cap.release

    
    


    

