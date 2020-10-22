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
        fgmask = backsub.apply(frame)
        cv2.line(frame,(0,480),(1280,480),(0,0,255),3)
        cv2.line(frame,(0,550),(1280,550),(0,0,255),3)
        cv2.rectangle(frame, (940,10), (1275, 95), (255,0,0), 3)

        contours,hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try : hierarchy = hierarchy[0]
        except: hierarchy=[]

        for contour,hier in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w>150 and h >150:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                if y>500 and y<530:
                    c+=1

        # cv2.putText(source_image,text,coordinates,font,size,color,thickness,better look)          
        cv2.putText(frame,"CAR:"+str(c),(945,85),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),3,cv2.LINE_AA)
        

        cv2.imshow("Car Counting",frame)
        cv2.imshow("fgmask",fgmask)
        
        if cv2.waitKey(40) & 0xFF==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()      