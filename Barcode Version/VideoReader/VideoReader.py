import cv2
from BarcodeDetection import IdentifyBarcode
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol

def cls():
    '''
    Clears terminal screen by printing 20 empty lines
    '''
    print("\n" * 20)

def decodeImage(image):
    data = []
    type = []
    codes = pyzbar.decode(image)

    for i in range(len(codes)):
        data.append(codes[i].data)
        type.append(codes[i].type)
    return data, type

# Main loop
cap = cv2.VideoCapture(0)
count = 0
threshold = 24
clearScreen = False

while True:
    count = count + 1

    _, frame = cap.read() # Read frame from webcam
    # box = IdentifyBarcode(frame)
    #
    # if len(box) > 0:
    #     cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)

    cv2.imshow("frame", frame)  # Display frame

    # Display data
    if count > threshold:
        codes, types = decodeImage(frame)
        print(str(len(codes)) + ' codes detected')

        if clearScreen:
            cls()
            clearScreen = False
        else:
            if len(codes) > 0:
                print(codes)
                print(types)
            clearScreen = True
        count = 0

    # Quit loop if requested
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print ("I quit!")
        break

cap.release()
cv2.destroyAllWindows()