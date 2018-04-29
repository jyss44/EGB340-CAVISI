import cv2
import qr_extractor as reader
import qrtools
import os
import time

cap = cv2.VideoCapture(0)

"""
Decodes a list of QR images
"""
def decodeImages(images):
    if not images:
        labels = []
        decoder = qrtools.QR()

        for image in images:
            decoder.decode(image) # Decode QR code from image
            labels.append(decoder.data) # Append data to list

        return labels
    else:
        return False

def cls():
    print("\n" * 20)

# Main loop
count = 0
threshold = 24
clearScreen = False

while True:
    count = count + 1

    _, frame = cap.read() # Read frame from webcam
    codes, frame = reader.extract(frame, True) # Extract QR codes from
    cv2.imshow("frame", frame) # Display

    labels = decodeImages(codes)

    # Display data
    if count > threshold:
        if clearScreen:
            cls()
            clearScreen = False
        else:
            print(labels)
            clearScreen = True
        count = 0

    # Quit loop if requested
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print ("I quit!")
        break

    # time.sleep(0.5) # Pause to let the shell catch up

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()