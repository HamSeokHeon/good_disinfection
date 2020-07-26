import cv2
import serial
import threading
import pygame
import time

'''
from __future__ import division
from linear_algebra import squared_distance, vector_mean
import random


############################ 군집 ###################################################
class KMeans:
    
    def __init__(self, k):
        self.k = k
        self.means = None
        
    def  classify(self, input):
        return min(range(self.k), key=lambda i:squared_distance(input, self.means[i]))
    
    def train(self, inputs):
        self.means = random.sample(inputs, self.k)
        assignments = None
        
    while True:
        new_assignments = map(self.classify, inputs)
        
        if assignments == new_assignments:
            return
        
        assignments = new_assignments
        
        for i in range(self.k):
            i_points = [p for p, a in zip(inputs, assignments) if a == i]
            if i_points:
                self.means[i] = vector_mean(i_points)
                
                
################################################################################
                
'''
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
body_cascade = cv2.CascadeClassifier('/home/pi/opencv/opencv-4.1.2/data/haarcascades/haarcascade_eye.xml')

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
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        body = body_cascade.detectMultiScale(img, 1.01,5)
        
        
        print(type(body))
        for(x,y,w,h)in body:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            
            #if(x+int(w/2)<=150): 
             #   cv2.circle(img,(80,120),30,(0,255,0),5)
              #  print("LEFT")
                
            #if(150<x+int(w/2)<=170):
            #    cv2.circle(img,(160,120),30,(0,255,0),5)
            #    print("MID")
                
            #if(170<x+int(w/2)<=320): 
            #    cv2.circle(img,(240,120),30,(0,255,0),5)
            #    print("RIGHT")
                
        text_temp = 101
        
        if str(type(body)) == "<class 'numpy.ndarray'>" :
            bang.play()
            time.sleep(2.0)
            
        cv2.imshow("VideoFrame",img)
    if cv2.waitKey(10)>=0:break


cap.release()
cv2.destroyAllWindows()








