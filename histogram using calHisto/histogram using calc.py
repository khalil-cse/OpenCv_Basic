import cv2
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('image/road.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
histr = cv2.calcHist([img], [2], None, [256], [0, 256])
# show the plotting graph of an image
plt.plot(histr)
plt.show()