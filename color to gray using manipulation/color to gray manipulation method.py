# Importing the OpenCV library
import cv2
import numpy as np
image = cv2.imread('image/road.jpg')
image1=cv2.resize(image,(500,500))
cv2.imshow('orginal',image1)
(row, col) = image1.shape[0:2]
print("size",row,col)
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
for i in range(row):
    for j in range(col):
        # Find the average of the BGR pixel values
        image1[i, j] = sum(image1[i, j]) * 0.33
cv2.imshow('After grayscale image using manipulation method',image1)
cv2.waitKey(0)
cv2.destroyAllWindows()