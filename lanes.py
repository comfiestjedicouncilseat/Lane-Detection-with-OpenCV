# Identifying lanes in an image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Function for applying Canny edge detection on an image
def canny(image):
    # Gray scale the image for single channel calculations
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Blur to reduce amount of edges detected, reduce image noise
    # Kernel size of 5 by 5
    # Deviation of 0
    blur = cv.GaussianBlur(gray, (5, 5), 0)

    # Run canny edge detection on the image
    # Threshold ratio of 1:3, or 50:150
    canny = cv.Canny(blur, 50, 150)

    return canny


# Function for creating a triangle mask for a region of interest
def region_of_interest(image):
    # Constants
    height = image.shape[0]
    width = image.shape[1]

    # Create the triangle shape, based on dimensions of the image
    # polygons must be an array, currently an array of one polygon
    polygons = np.array([
        [(200, height), (width - 200, height), (600, 250)]
        ])

    # Create a blank image with the same size as the passed in image
    mask = np.zeros(image.shape, dtype="uint8")

    # Drawing a triangle on the image with fillPoly, accepts array of polygons
    cv.fillPoly(mask, polygons, 255)

    return mask


# Read an image - will change to video later
img = cv.imread("test_image.jpg")

# Creating a copy of the original image for modification
lane_img = np.copy(img)

# Canny the image
canny = canny(lane_img)
cv.imshow("Edges Detected", canny)

# Create the mask for the image
img_roi = region_of_interest(canny)
cv.imshow("ROI", img_roi)

cv.waitKey(0)
