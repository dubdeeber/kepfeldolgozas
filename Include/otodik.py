import numpy as np
import random as r
import cv2
open_mode=0
img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\noisy_car.jfif",open_mode)
#img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\El Gatto.jpg",open_mode)
img2=cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",0)
img = cv2.medianBlur(img,5)
imgT = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2) ##only for black and white
#ret, imgT=cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

res=np.vstack((img,imgT))
cv2.imshow("result",img)
cv2.imshow("mod",imgT)


cv2.waitKey(0)


