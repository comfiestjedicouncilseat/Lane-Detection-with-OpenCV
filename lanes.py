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
cv.imshow("Gray Road", gray)

# Blur to reduce amount of edges detected
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# Run canny edge detection on the image
canny = cv.Canny(gray, 125, 175)
cv.imshow("Edges Detected", canny)


cv.waitKey(0)
