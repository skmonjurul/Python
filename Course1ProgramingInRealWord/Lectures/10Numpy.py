#what is numpy?
ans: numpy is the base library for many other python libraries.

#read an image using cv2
ans:
import cv2
for i in dir(cv2):
    if "read" in i:
        print(i)
im_g=cv2.imread("C:\\Users\\sabyasachi\\Desktop\\Python\\sampleFiles\\smallgray.png",0)  -> 1 for gray_scala, 2 for colour bgr
type(im_g)

#indexing and slicing