# Import packages
import numpy as np
import argparse
import cv2

def IdentifyBarcode(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the Scharr gradient magnitude representation of the images
    # in both the x and y direction
    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # Subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    # Blur and threshold the image
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # Close gapes in thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))  # Kernal for erosion + dilation
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Remove small blobs with a series of erosions & dilations
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    # Find the contours in the thresholded image, then sort the contours
    # by their area, keeping only the largest one
    (_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    return box


# Load image
image = cv2.imread('barcode_01.jpg')
print(type(image))

box = IdentifyBarcode(image)

cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Identified barcode", image)

# Decode image

# Video frame
cap = cv2.VideoCapture(0)
_, frame = cap.read()
cap.release()

box = IdentifyBarcode(frame)

box = IdentifyBarcode(frame)

if len(box) > 0:
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)

cv2.imshow('VideoCap', frame)

# While loop to prevent windows from closing
# Press q to exit
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print ("I quit!")
        break
