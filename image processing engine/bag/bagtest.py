import cv2
import numpy as np
import time
import os

bag = cv2.CascadeClassifier('cascades/bag.xml')

cap = cv2.VideoCapture('12.MP4')
check = []
main_start = time.time()
while True:
        ret, image = cap.read()
        #image = image[200 : , : ]
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        baggage = bag.detectMultiScale(gray,2,3)
        for(x,y,w,h) in baggage:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                temp_cood = [x,y,time.time()]
                check.append(temp_cood)
                for a in check:
                        #print " Spotted"
                        if (temp_cood[0] == a[0] and temp_cood[1] == a[1]) :
                                if (temp_cood[2] > a[2] + 15):
                                        #print ""
                                        os.system("vlc alert.mp3")
                                        print "WARNING ! /n AN UNATTENDED BAG HAS BEEN DETECTED"
					cv2.imshow('bag',image[y:y+h,x:x+w])
                        else:
                                check.append(temp_cood)
                                continue

                #check.append(x,y,time.time())
        end = time.time()
        cv2.imshow('Cam1',image)
        print (end-main_start)
        k = cv2.waitKey(27) & 0xFF
        if k == 27:
                break

cap.release()
cv2.destroyAllWindows()
