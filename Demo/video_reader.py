import cv2
import qr_extractor as reader
import qrtools

"""
Decodes a list of QR images
Takes an array of QR images
Returns False if input array is empty
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

"""
Clears terminal by printing out several empty lines
"""
def cls():
    print("\n" * 20)

# Main loop

# Constants
count = 0
threshold = 24
clearScreen = False

# Aquire webcam capture
webcamID = 1 # 0 for build in webcam, 1 for USB webcam
cap = cv2.VideoCapture(1)

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

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()