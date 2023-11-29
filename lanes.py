# Identifying lanes in an image
import cv2 as cv
import numpy as np

# Read an image - will change to video later
img = cv.imread("test_image.jpg")
cv.imshow("Test Road Image", img)

# Creating a copy of the original image for modification
lane_img = np.copy(img)

# Gray scale the image for single channel calculations
gray = cv.cvtColor(lane_img, cv.COLOR_BGR2GRAY)

# Blur to reduce amount of edges detected, reduce image noise
# Kernel size of 5 by 5
# Deviation of 0
blur = cv.GaussianBlur(gray, (5, 5), 0)

# Run canny edge detection on the image
# Threshold ratio of 1:3, or 50:150
canny = cv.Canny(blur, 50, 150)
cv.imshow("Edges Detected", canny)


cv.waitKey(0)
