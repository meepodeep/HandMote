import pyautogui as pag
import HandMote as hm
import cv2 

while True:
    pag.moveTo(hm.cxInverse, hm.cy,.2)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()