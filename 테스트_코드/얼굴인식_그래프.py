from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
#import sklearn
'''
X, y = make_blobs(random_state=0, n_samples=12)

dbscan = DBSCAN()
clusters = dbscan.fit_predict(X)
print("클러스터 레이블:\n{}".format(clusters))
'''

import cv2
import numpy as np
cap= cv2.VideoCapture(0)
body_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#if cap.isOpened()==False:
 #   exit()

face_points = np.empty((0,2) , int)

 
i = 0


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
            
            face_points = np.append(face_points, np.array([[x+int(w/2),y+int(h/2)]]),axis=0)
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.line(img,(x+int(w/2),y+int(h/2)),(x+int(w/2),y+int(h/2)),(0,255,0),5)
    i+=1
    if i>20:
        break
            

    cv2.imshow("VideoFrame",img)
    if cv2.waitKey(10)>=0:break

print(face_points)
cap.release()
cv2.destroyAllWindows()


###########################################################dbscan##
dbscan = DBSCAN(min_samples=16, eps=20)
clusters = dbscan.fit_predict(face_points)

#idx_outlier = dbscan.labels_ == -1

#idx_lier = dbscan.labels_ >= 0
#print(idx_lier)
print(clusters)
print(type(clusters))

if 0 in clusters:
    print("OK")


#plt.scatter(face_points[idx_lier, 0], face_points[idx_lier, 1] ,marker='o', s=50)
plt.scatter(face_points[:, 0], face_points[:, 1], c=clusters,linewidth=2,marker='o', s=50)
#plt.scatter(face_points[idx_outlier, 0], face_points[idx_outlier, 1],marker='x',linewidth=2,s=50)
plt.xlabel("$X_1$")
plt.ylabel("$X_2$")
plt.show()
###########################################################dbscan#










'''


print(face_points[:,0])

print(face_points[:,1])
#X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
#print(X)

plt.title("세개의 클러스터를 가진 가상 데이터")
#X, y = make_blobs(n_samples=300, n_features=2, centers=3, random_state=1)
#plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=100,
#            edgecolor="k", linewidth=2)
plt.scatter(face_points[:, 0], face_points[:, 1])
plt.xlabel("$X_1$")
plt.ylabel("$X_2$")
plt.show()
'''