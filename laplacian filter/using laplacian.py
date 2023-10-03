import cv2
import numpy as np

# Load an image
image = cv2.imread('image/car1.jpg')
image=cv2.resize(image,(500,500))

# Convert the image to grayscale (Laplacian filter works on grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Laplacian filter
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Convert the Laplacian result back to an 8-bit image
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Display the original image and the Laplacian result
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian', laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
