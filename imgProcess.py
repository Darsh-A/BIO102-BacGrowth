"""
This is the Image processing code written in opencv-python which 
detects the diameter of the bacteria colonies
just run this python file to see the output
"""


import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('media\images\main\BacteriaGrowth_ManimCE_v0.17.3.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply image thresholding to obtain a binary image
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(image=binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# Define the minimum distance between the centers of detected contours to consider them part of the same group
min_distance = 15  # Adjust this value as needed

# Create an empty list to store the grouped contour indices
grouped_contours = []

# Iterate through each contour and check if it should be grouped with any existing group
for i, contour in enumerate(contours):
    # Calculate the center of the contour using the moments
    moments = cv2.moments(contour)
    if moments["m00"] > 0:
        cx = int(moments["m10"] / moments["m00"])
        cy = int(moments["m01"] / moments["m00"])

        # Check if the contour should be grouped with any existing group
        group_index = None
        for j, grouped_contour in enumerate(grouped_contours):
            # Calculate the center of the grouped contour
            grouped_moments = cv2.moments(grouped_contour)
            if grouped_moments["m00"] > 0:
                grouped_cx = int(grouped_moments["m10"] / grouped_moments["m00"])
                grouped_cy = int(grouped_moments["m01"] / grouped_moments["m00"])

                # Calculate the distance between the centers
                distance = np.sqrt((grouped_cx - cx) ** 2 + (grouped_cy - cy) ** 2)

                # If the distance is less than the minimum distance, group the contours
                if distance < min_distance:
                    group_index = j
                    break

        # Add the contour to an existing group or create a new group
        if group_index is not None:
            grouped_contours[group_index] = np.concatenate((grouped_contours[group_index], contour))
        else:
            grouped_contours.append(contour)

# Draw circles around each group of contours and find the diameter of the circle
circle_positions = []
circle_diameters = []
data = []
for grouped_contour in grouped_contours:
    # Fit a circle to the grouped contour
    (x, y), radius = cv2.minEnclosingCircle(grouped_contour)
    center = (int(x), int(y))
    radius = int(radius)

    # Calculate the diameter of the circle
    diameter = 2 * radius
    num_points = len(grouped_contour)

    # Draw the circle on the image
    if (diameter > 9) & (diameter < 100):
        cv2.circle(image, center, radius, (0, 255, 0), 2)

        circle_positions.append(center)
        circle_diameters.append(diameter)
        data.append([diameter, center[0], center[1], num_points])


np.savetxt('data.txt', data, fmt='%d', delimiter=',')   # diameter / center_x / center_y / num_points
# Display the image with the circles
image_copy = image.copy()
print(circle_positions)
print(circle_diameters)
cv2.imshow("Grouped Contours", image)
cv2.imwrite('media/images/main/colonies.jpg', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
