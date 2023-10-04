import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('image/road.jpg')

# Resize the image
image1 = cv2.resize(image, (300, 300))

# Create a list of filtered images
filters = [
    ('Orginal Image',image1),
    ('Gaussian Blurring', cv2.GaussianBlur(image1, (7, 7), 0)),
    ('Median Blurring', cv2.medianBlur(image1, 5)),
    ('Bilateral Blurring', cv2.bilateralFilter(image1, 9, 75, 75))
]

# Set the figure size
plt.figure(figsize=(8, 5))

# Display the images in a loop
for i, (filter_name, filtered_image) in enumerate(filters, 1):
   # plt.subplot(1, len(filters), i)
    plt.subplot(2,2,i)
    plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
    plt.title(filter_name)
    plt.axis('off')

# Show the figure with all the images
plt.show()
