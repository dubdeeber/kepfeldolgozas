import numpy as np
import random as r
import cv2
open_mode=1
Image = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic.jfif",open_mode)
Image2=cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic2.jpg",open_mode)
Result=Image.copy()
print(Image.shape==Image2.shape)
for i in range (int(Image.shape[0]/10)*3):
#for i in range (int(Image.shape[0])):
        for k in range (2) :
            for j in range (Image.shape[1]) :
                #if (r.randint(0,10)<3):
                    Result[i][j][k]=Image2[i][j][k]

cv2.imshow("Test",Result)

#cols, rows, dim=Image.shape
#print(cols, rows, dim)
#b=np.zeros(Image.shape,dtype=np.uint16)
#b=Image.copy()
#no_blue=b
#no_blue[:,:,0] = np.zeros([no_blue.shape[0], no_blue.shape[1]])
#hsv=cv2.cvtColor(b,cv2.COLOR_BGR2HSV)
#print(hsv)
#cv2.imshow("HSV Image",hsv)
#cv2.imshow("Original",Image)
#cv2.imshow("No blue in img",no_blue)
#cv2.imshow("HSV2BGR",cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR))
cv2.waitKey(0)
