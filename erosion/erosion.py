# Importing the OpenCV library
import cv2
import numpy as np
image = cv2.imread('video/road.jpg')
image1=cv2.resize(image,(500,500))
cv2.imshow('orginal',image1)
# Creating kernel
kernel = np.ones((5, 5), np.uint8)

# Using cv2.erode() method
image2 = cv2.erode(image1, kernel)
cv2.imshow('After erosion image:', image2)


cv2.waitKey(0)
cv2.destroyAllWindows()
