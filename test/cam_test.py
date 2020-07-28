import cv2
cap= cv2.VideoCapture(0)
body_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#if cap.isOpened()==False:
 #   exit()



while True:
    ret,img=cap.read()

    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('preview',img)
    #if cv2.waitKey(10)>=0:
     #   break
    if ret:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        body = body_cascade.detectMultiScale(img, 1.01, 10)
        for (x,y,w,h) in body:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            #cv2.line(img,(x+int(w/2),y+int(h/2)),(x+int(w/2),y+int(h/2)),(0,255,0),5)
            

    cv2.imshow("VideoFrame",img)
    if cv2.waitKey(10)>=0:break

cap.release()
cv2.destroyAllWindows()







