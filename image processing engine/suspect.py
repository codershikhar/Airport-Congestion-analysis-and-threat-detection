import cv2
import os
from PIL import Image
import numpy as np
print("loading face recognizer database")
faceRecognizer = cv2.face.createLBPHFaceRecognizer()
faceDetect = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

labels = os.listdir('red_corner')
img = []    #store list of numpy images
labelint=[] #store converted labels in terms of numbers
for lab in labels:
    imgpil = Image.open("red_corner/"+lab).convert('L')
    simage = np.array(imgpil, 'uint8')  #subject image
    faces = faceDetect.detectMultiScale(simage)
    for (x,y,w,h) in faces:
        img.append(simage[y:y+h, x:x+w])
        labelint.append(int(lab.split(".")[0].replace("subject", "")))

print("training...")
#print(type(labels[1]))
#print(type(img[12]))
labelint = np.array(labelint)
faceRecognizer.train(img, labelint)
print("training completed")

cap = cv2.VideoCapture(0)
ret,frame = cap.read()

while ret:
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facesDetected = faceDetect.detectMultiScale(grayFrame)
    for x,y,w,h in facesDetected:
        match_label, dist = faceRecognizer.predict(grayFrame[y:y+h,x:x+w])
        print("label : "+str(match_label)+"dist"+str(dist))
        if match_label == 16 and dist<50:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,"Admin",(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
	elif match_label == 17 and dist<65:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,"Shaunak",(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        if dist in range(55,100):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "analyzing id unknown", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("webcam",frame)
    cv2.waitKey(1)
    ret,frame=cap.read()
