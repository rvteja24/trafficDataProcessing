import numpy as np
import cv2 as cv

img = cv.imread("input/traffic_signal.jpeg")
imgCopy=img.copy()
imgCopy2=img.copy()
print(img)
cv.imshow("Display Output", img)
cv.waitKey(0)
car_cascade = cv.CascadeClassifier('../trainingCode/trainedClassifier/cars.xml')

grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY);
ret,thresh = cv.threshold(grey,127,255,0)
cv.imshow("Display Output", grey)
cv.waitKey(0)
contours, hierarchy =  cv.findContours(thresh,cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
print(contours)
print(hierarchy)
       
cv.drawContours(imgCopy,contours,-1,(255,0,0),1)
cars = car_cascade.detectMultiScale(grey, 1.1, 1)
     
    # To draw a rectangle in each cars
for (x,y,w,h) in cars:
        cv.rectangle(imgCopy2,(x,y),(x+w,y+h),(0,0,255),2)

cv.imshow("Display Output", imgCopy2)
cv.waitKey(0)

cv.imshow("Display Output", imgCopy)
cv.waitKey(0)
