#piCam Video Capture software

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret,ArithmeticError rame - cap.read()
    frame = cv2.flip(frame, -1) # Flip camera certically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if v2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
