""" -*- coding: utf-8 -*-
    @author: omerkocadayi 
    https://github.com/omerkocadayi
    https://www.linkedin.com/in/omerkocadayi/ """

import cv2

vid = cv2.VideoCapture("cars.mp4")
backsub = cv2.createBackgroundSubtractorMOG2()
c = 0

while True:
    ret,frame = vid.read()
    if ret:
        mask = backsub.apply(frame)
        cv2.line(frame,(0,470),(1280,470),(0,0,255),3)
        cv2.line(frame,(0,520),(1280,520),(0,0,255),3)
        cv2.rectangle(frame, (940,10), (1275, 95), (255,0,0), 3)

        contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try : hierarchy = hierarchy[0]
        except: hierarchy=[]

        for contour,hier in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w>150 and h >150:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                if y>490 and y<525:
                    c+=1
                    
        try : hierarchy = hierarchy[1]
        except: hierarchy=[]


        #cv2.putText(source_image,text,coordinates,font,size,color,thickness,better look)          
        cv2.putText(frame,"CAR:"+str(c),(945,85),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),3,cv2.LINE_AA)
        
        cv2.imshow("Mask",mask)
        cv2.imshow("Frame",frame)
                
        if cv2.waitKey(40) & 0xFF==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()      