import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

  
def bodyDetect():
    body_cascade = cv2.CascadeClassifier('lbpcascade_full.xml')
    try:
        cap=cv2.VideoCapture(1)

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


        #Show the Cam Screen
        cv2.imshow('frame',frame)
        
        #Exit when you put ESC Key
        k=cv2.waitKey(30) & 255;
        if k==27:
            break;
    cap.release()

    cv2.destroyAllWindows()
bodyDetect()