# Identifying lanes in an image
import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt


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

    # Cropping out the region of interest using a bitwise AND
    # between the canny'd image and the mask
    cropped = cv.bitwise_and(image, mask)

    return cropped


# Function for taking the Hough Lines, and applying them to a blank image
def display_lines(image, lines):
    # Create a blank image
    line_image = np.zeros_like(image)
    # Check if there are any lines
    if lines is not None:
        # Loop through all lines in the lines array
        for line in lines:
            # Change every line from 2D array to 4 variables
            x1, y1, x2, y2 = line.reshape(4)

            # Draw the line on the blank image
            cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=10)

    return line_image


# Read an image - will change to video later
img = cv.imread("test_image.jpg")

# Creating a copy of the original image for modification
lane_img = np.copy(img)

# Canny the image
canny = canny(lane_img)

# Create the mask for the image
cropped_img = region_of_interest(canny)

# Creating the Hough Lines
# 2 for pixel length (Rho), pi/180 for 1 degree (Radians)
# Threshold: min num of votes needed to become a line (100 in this case)
# Also need to pass in an empty array
# minLineLength: lines less than 40 pixels are rejected
# maxLineGap: max num of pixels in a gap, otherwise, connect the lines
lines = cv.HoughLinesP(cropped_img, 2, np.pi/180, 100, np.array([]),
                       minLineLength=40, maxLineGap=5)

# Create a blank image with the Hough lines drawn
line_img = display_lines(lane_img, lines)

# Overlay the image with lines, with the original image
result = cv.addWeighted(lane_img, 0.8, line_img, 1, 1)
# result = cv.bitwise_or(lane_img, line_img)

# Show the image
cv.imshow("region", result)

cv.waitKey(0)
