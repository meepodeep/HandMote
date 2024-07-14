import numpy as np
import cv2
import mediapipe as mp
import time 
import pyautogui as pag
import threading

cxInverse = 0
pag.FAILSAFE = False
cx_global = 0
cy_global = 0
ret = False
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

   
def FindHands(cam,):
    global cx_global
    global cy_global
    while True:
        
        ret, frame = cam.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1920, 1080))
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cy_global = cy
                    cx_global = cx
                    if id == 0:
                        cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    
                    if id == 2:
                        cv2.circle(frame, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                        
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    
            

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
    
def MoveMouse(cxInverse,):
    global cx_global
    global cy_global
    while True:
        print(cx_global, cy_global)
        cxInverse = (cx_global *-1) + 1920
        pag.moveTo(2*cxInverse, 2*cy_global,.01)
        
        
if __name__ == '__main__':
    t1 = threading.Thread(target = FindHands,args=(cap,))
    t2 = threading.Thread(target = MoveMouse,args=(cxInverse,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

     