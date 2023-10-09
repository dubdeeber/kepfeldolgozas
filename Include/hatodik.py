import numpy as np
import random as r
import cv2
open_mode=0
#img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\noisy_car.jfif",open_mode)
#img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\El Gatto.jpg",open_mode)

img=cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\El Gatto.jpg",0)
imgT = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
kernel = np.ones((3, 3), np.uint8) 

imgB=cv2.dilate(imgT, kernel, iterations=1)
res=cv2.erode(imgB, kernel, iterations=5) 
#opening
#imgA=cv2.threshold(img, 0, 255, 
#                     cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1] 
#imgB=cv2.morphologyEx(imgA, cv2.MORPH_OPEN, 
#                          kernel, iterations=5)
#closing
#
#imgA = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]  
#imgB = cv2.morphologyEx(imgA, cv2.MORPH_CLOSE, kernel, iterations=2) 

#for i in range (int(img.shape[0]/100)*33): #non random
for i in range (int(img.shape[0])): # random
            for j in range (img.shape[1]) :
                if (r.randint(0,100)<33): #if random, needed
                    res[i][j]=img[i][j]


#res=np.hstack((res,imgT))
cv2.imshow("OG",img)
cv2.imshow("res",res)
#cv2.imshow("A",imgT)
#cv2.imshow("B",imgB)


cv2.waitKey(0)


