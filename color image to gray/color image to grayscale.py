# Importing the OpenCV library
import cv2
image = cv2.imread('image/road.jpg')
image1=cv2.resize(image,(500,500))
cv2.imshow('orginal',image1)
image=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
cv2.imshow('After grayscale image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()