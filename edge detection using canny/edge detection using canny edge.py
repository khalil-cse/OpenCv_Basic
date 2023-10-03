
import cv2

image = cv2.imread('image/road.jpg')

image1=cv2.resize(image,(500,500))
cv2.imshow('orginal',image1)
# Convert BGR image to RGB
image_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
edges = cv2.Canny(image_rgb, threshold1=80,threshold2=100)


cv2.imshow('Weighted Image', edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
