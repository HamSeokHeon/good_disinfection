import cv2
import serial
import threading
import pygame
import time
import numpy as np
from sklearn.cluster import DBSCAN

pygame.mixer.init()
bang = pygame.mixer.Sound("../cleanHand.wav")

###########################################
ser = serial.Serial('/dev/ttyACM0',9600)
#while True:
#    ReadText = ser.readline()
#    if ReadText[0] == 102:
#        print("aaaaaaaaaaaaaaaa")
#333333333################################3
cap= cv2.VideoCapture(-1)
body_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#if cap.isOpened()==False:
#   exit()
text_temp = 101

def getText():
    global text_temp
    while True:
        text_temp = ser.readline()[0];
        
 
thread = threading.Thread(target=getText)
thread.daemon = True
thread.start()

ReadText = 102;
while True:
    ret,img=cap.read()
    if ReadText == text_temp:
        face_points = np.empty((0,2) , int)
        temp_W_H = []
        i=0
        while True:
            if ret:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                body = body_cascade.detectMultiScale(img, 1.01, 10)
                for (x,y,w,h) in body:
                    
                    
                    if w>100 and h>100:
                        face_points = np.append(face_points, np.array([[x+int(w/2),y+int(h/2)]]),axis=0)
                    
                    
                    
                    
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.line(img,(x+int(w/2),y+int(h/2)),(x+int(w/2),y+int(h/2)),(0,255,0),5)
            i+=1
            if i>5:
                break 
            ####################3
        text_temp = 101
        
        if face_points.tolist(): ##리스트가 비어있을 경우 에러가남 예외처리
            dbscan = DBSCAN(min_samples=3, eps=20)
            clusters = dbscan.fit_predict(face_points)
            if 0 in clusters:
                bang.play()
                time.sleep(2.0)
            
        #cv2.imshow("VideoFrame",img)
    if cv2.waitKey(10)>=0:break


#cap.release()
#cv2.destroyAllWindows()








