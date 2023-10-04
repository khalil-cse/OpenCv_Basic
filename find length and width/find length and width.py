import cv2

# Load the image
image = cv2.imread('image/rice.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through detected contours
for contour in contours:
    # Calculate the bounding box around the object
    x, y, w, h = cv2.boundingRect(contour)

    # Calculate the length and width
    length = w
    width = h

    # Draw a bounding box around the object
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green bounding box

    # Optionally, you can print or use the length and width for further analysis
    print(f"Object Length: {length}, Object Width: {width}")

# Display the image with bounding boxes
cv2.imshow('Objects with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
