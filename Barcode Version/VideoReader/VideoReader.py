import cv2
from BarcodeDetection import IdentifyBarcode
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol
import math

def cls():
    '''
    Clears terminal screen by printing 20 empty lines
    '''
    print("\n" * 20)

def decodeImage(image):
    data = []
    codes = pyzbar.decode(image)

    for i in range(len(codes)):
        if verifyCode(codes[i].data):
            data.append(codes[i].data)
    return data

def verifyCode(code):
    codeStr = str(code)
    length = len(codeStr)
    checkDigit = int(codeStr[length-2])
    codeStr = codeStr[2:length-1]

    if len(codeStr) == 13:
        sumEven = sumEvens(codeStr) * 3
        sumOdd = sumOdds(codeStr)

        total = (sumEven + sumOdd) % 10

        if (checkDigit + total) % 10 == 0:
            return True
        else:
            return False
    else:
        return False


def sumEvens(numStr):
    length = len(numStr)
    sum = 0

    for i in range(0, math.floor(length/2)):
        index = i * 2 + 1
        sum = sum + int(numStr[index])

    return sum

def sumOdds(numStr):
    length = len(numStr)
    sum = 0

    for i in range(0, math.floor(length / 2)):
        index = i * 2
        sum = sum + int(numStr[index])

    return sum

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
        codes = decodeImage(frame)
        print(str(len(codes)) + ' codes detected')

        if clearScreen:
            cls()
            clearScreen = False
        else:
            if len(codes) > 0:
                print(codes)
            clearScreen = True
        count = 0

    # Quit loop if requested
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print ("I quit!")
        break

cap.release()
cv2.destroyAllWindows()