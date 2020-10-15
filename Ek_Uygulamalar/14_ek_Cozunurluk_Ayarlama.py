""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2
window_name = "Live"
cv2.namedWindow(window_name)

cap = cv2.VideoCapture(0)

print("Original Resolution : "+str(cap.get(3))+" * "+str(cap.get(4)))

cap.set(3, cap.get(3) + cap.get(3)*0.3) #or cap.get(3)*1.3
cap.set(4, cap.get(4) + cap.get(4)*0.3) #or cap.get(4)*1.3

print("\n+30%.. Resolution : "+str(cap.get(3))+" * "+str(cap.get(4)))

while 1:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    cv2.imshow(window_name, frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()