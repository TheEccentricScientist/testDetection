#import numpy as np
import cv2
#from firebase import firebase                          
#from matplotlib import pyplot as plt
#import pyimgur
#CLIENT_ID = "f0e83904a2dee5a"


#im = pyimgur.Imgur(CLIENT_ID)
#uploaded_image = im.upload_image("t+u+a.jpg", title="Uploaded with PyImgur")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

image = cv2.imread('tino.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = image[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for(ex,ey,ew,eh) in eyes:
		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

numfaces =len(faces)
print numfaces

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
