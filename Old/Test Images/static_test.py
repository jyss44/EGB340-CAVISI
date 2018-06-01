import cv2
import numpy as np
import qr_extractor as reader

# Load image
img = cv2.imread('testimg.jpg')

# Display image

# Extract qr code

codes, frame = reader.extract(img, True)
cv2.imshow('frame', frame)
print len(codes)

cv2.waitKey(0)
# Display



