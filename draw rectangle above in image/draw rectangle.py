
# importing cv2
import cv2

# Reading an image in default mode
image = cv2.imread("image/car1.jpg")
image1=cv2.resize(image,(500,500))

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (100, 50)

# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (300, 300)

# Green color in BGR
color = (0, 0, 250)

# Line thickness of 9 px
thickness = 5
image2 = cv2.rectangle(image1, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name, image2)
cv2.waitKey(0)
cv2.destroyAllWindows()