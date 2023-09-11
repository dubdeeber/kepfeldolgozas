import numpy as np
import cv2
open_mode=1
Image = cv2.imread("C:\\Users\\student\\dubdeeber\\kepfeldolgozas\\pic.jfif",open_mode)



cols, rows, dim=Image.shape
name= np.asarray(Image.shape,dtype=np.uint16)
b=np.zeros(Image.shape,dtype=np.uint16)
b=Image
cv2.imshow("test",b)
cv2.waitKey(0)
