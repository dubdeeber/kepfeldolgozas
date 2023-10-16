import cv2
import numpy as np
import random




def Elso():
    img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",1)
    img = cv2.medianBlur(img,5)
    cv2.imshow("img",img)
    cv2.waitKey()

def Masodik():
    img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",0)
    kernel = np.ones((3, 3), np.uint8) 

    imgD=cv2.dilate(img, kernel, iterations=1)
    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    cv2.imshow("img",img)
    cv2.waitKey()

def Harmadik():
    img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",0)    
    imgC = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    imdD=cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
    imgA=cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
    imgB=cv2.threshold(img, 0, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)[1] 
    cv2.imshow("imgA",imgA)
    cv2.imshow("imgB",imgB)
    cv2.imshow("imgC",imgC)
    cv2.waitKey()

def Negyedik():
    img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",1)
    percent=int(input("százalék:"))
    imgT=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgT[:,:,2] *= np.uint8(percent/100)
    cv2.imshow("imgC",imgT)
    cv2.waitKey()

def Otodik():
    img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",0)    
    (T,imgC) = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    #T A maszk



#Elso()
#Masodik()
#Harmadik()
#Negyedik()
#Otodik()
