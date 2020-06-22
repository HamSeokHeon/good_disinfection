import cv2
import serial
###########################################
ser = serial.Serial('/dev/ttyACM1',9600)
#while True:
#    ReadText = ser.readline()
#    if ReadText[0] == 102:
#        print("aaaaaaaaaaaaaaaa")
#333333333################################3
cap= cv2.VideoCapture(-1)
body_cascade = cv2.CascadeClassifier('/home/pi/project/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#if cap.isOpened()==False:
 #   exit()
ReadText = 102;
while True:
    #if ser.readline()[0] == 102:
    #    ReadText = ser.readline()[0]
    ret,img=cap.read()

    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('preview',img)
    #if cv2.waitKey(10)>=0:
     #   break
    if ReadText == 102:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        body = body_cascade.detectMultiScale(img, 1.01, 10)
        #cv2.line(img,(160,0),(160,240),(0,255,0),5)
        for (x,y,w,h) in body:
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            #cv2.line(img,(x+int(w/2),y),(x+int(w/2),y+h),(0,255,0),5)
            if(x+int(w/2)<=150): 
                #cv2.circle(img,(80,120),30,(0,255,0),5)
                print("LEFT")
            if(150<x+int(w/2)<=170):
                #cv2.circle(img,(160,120),30,(0,255,0),5)
                print("MID")
            if(170<x+int(w/2)<=320): 
                #cv2.circle(img,(240,120),30,(0,255,0),5)
                print("RIGHT")

    cv2.imshow("VideoFrame",img)
    if cv2.waitKey(10)>=0:break

cap.release()
cv2.destroyAllWindows()







