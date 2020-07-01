# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 14:47:21 2020

@author: rlawl
"""
import cv2
import time
import pyautogui as pag

def start_timer():
    t_start = int(time.time())
    return t_start

font = cv2.FONT_HERSHEY_SIMPLEX

  
def bodyDetect(cascade, cTab, oTab, mute):
    switch =0 #switch OFF
    body_cascade = cv2.CascadeClassifier(cascade+'.xml')
    try:
        cap=cv2.VideoCapture(0)

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        print('width {0}, height {1}, fps {2}'.format(width, height, fps))
        
    except:
        print('카메라 로딩 실패')
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            return

        #Convert gray scale
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #7 by 7 kernel, sigma = 1
        blur =  cv2.GaussianBlur(gray,(7,7), 1)
        #histogram Equalization
        eq = cv2.equalizeHist(blur)
        
        body = body_cascade.detectMultiScale(eq,1.1, 10, 0,(75, 75)) 


        #(x,y,width, height
        for (x,y,w,h) in body:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 3, 4, 0)
            cv2.putText(frame, 'People Detected', (x-5, y-5), font, 0.9, (255,255,0),2)


        #if people don't detect, variable 'body' type is tuple,
        #else, body type is nparray
        
        
        #switch = OFF, people Detecting
        if (type(body)!=tuple and switch==0):
            if mute==True:    
                pag.press('volumemute')
                print("Mute On")
            #move to Tab what you want
            pag.hotkey('win',cTab)
            
            switch = 1

            
        #switch = ON, nothing Detected
        elif(type(body)==tuple and switch==1):
            if mute==True:    
                pag.press('volumemute')
                print("Mute OFF")
            #move to Tab what your original Tab
            pag.hotkey('win',oTab)
            
            switch = 0
        else:
            pass
        
        #Show the Cam Screen
        cv2.imshow('frame',frame)
        
        #Exit when you put ESC Key
        k=cv2.waitKey(30) & 255;
        if k==27:
            break;
    cap.release()

    cv2.destroyAllWindows()