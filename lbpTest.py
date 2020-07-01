# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:08:55 2020

@author: rlawl
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
font = cv2.FONT_HERSHEY_SIMPLEX

fig = plt.figure()
rows = 5
cols = 10
body_cascade = cv2.CascadeClassifier('lbpcascade_full.xml')

def detect(img):
    
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur =  cv2.GaussianBlur(gray,(7,7), 1)
    eq = cv2.equalizeHist(blur)
    body = body_cascade.detectMultiScale(eq,1.1, 10, 0,(75, 75)) 
    

    for (x,y,w,h) in body:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3, 4, 0)
        cv2.putText(img, 'People Detected', (x-5, y-5), font, 0.9, (255,255,0),2)



for i in range (50):
    img = cv2.imread("picture/{0}.bmp".format(i+20))
    detect(img)
    ax = fig.add_subplot(rows, cols, i+1)
    ax.axis("off")
    ax.set_aspect('equal')
    ax.imshow(img)
    
plt.show
cv2.waitKey(0)
cv2.destroyAllWindows()


        