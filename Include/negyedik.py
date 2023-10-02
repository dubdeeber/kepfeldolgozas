import numpy as np
import random as r
import cv2
open_mode=1
img = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic.jfif",open_mode)
img2=cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",0)

#out= cv2.boxFilter(img,-222,(50,50))#box
print(img.shape[0],img.shape[1])
out= cv2.GaussianBlur(img,(img.shape[0],img.shape[1]-1),2) # gauss
#out= cv2.medianBlur(img,25)


##value=3 always odd
## sigma_value=2
## cv2.boxFilter(input, -1 , (value, value))
## cv2.GaussianBlur(input, (value, value), sigma_value)
## cv2.medianBlur(input,value)
##

cv2.imshow("original",img)
#cv2.imshow("Test",out)
#cv2.imshow("Test",out)
hist=cv2.equalizeHist(img2) #grayscaleonly!!!
res=np.hstack((img2,hist))
cv2.imshow("Test2",res)
#unsharpened= cv2.addWeighted(img,1.5,out,-0.5, 0)
#cv2.imshow("Test2",unsharpened)

#ret,thresh= cv2.threshold(img,20,255,cv2.THRESH_BINARY_INV)
#thresh= cv2.threshold(img,127 ,255,cv2.THRESH_BINARY_INV)
#cv2.imshow("Test2",thresh)

#blurred=cv2.blur(img,(25,25))
#cv2.imshow("test",blurred)
#sharp=cv2.addWeighted(img,1.5,out,-0.5, 0)
#cv2.imshow("test2",sharp)


cv2.waitKey(0)


