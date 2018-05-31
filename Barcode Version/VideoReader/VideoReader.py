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
    '''
    Detects and decodes all barcodes in an image
    :param image: Tuple, or numpy array representing an image
    :return: List of byte objects representing barcode numbers
    '''
    data = []
    codes = pyzbar.decode(image)

    for i in range(len(codes)):
        if verifyCode(codes[i].data):
            data.append(codes[i].data)
    return data

def verifyCode(code):
    '''
    Verifies a barcode as valid with a checksum algorithm
    :param code: Barcode number as byte object
    :return: True if barcode passes checksum, False otherwise
    '''
    codeStr = str(code)
    length = len(codeStr)
    checkDigit = int(codeStr[length-2])
    codeStr = codeStr[2:length-1]

    if len(codeStr) == 13: # Barcode must have 13 digits to be of EAN13 standard
        sumEven = sumEvens(codeStr) * 3 # Sum even digits, with a weight
        sumOdd = sumOdds(codeStr)

        total = (sumEven + sumOdd) % 10

        if (checkDigit + total) % 10 == 0: # Sum of total + check digit must be multiple of 10
            return True
        else:
            return False
    else:
        return False


def sumEvens(numStr):
    '''
    Sums the even positioned digits of a number
    :param numStr: Number, as a string
    :return: sum of even position numbers
    '''
    length = len(numStr)
    sum = 0

    for i in range(0, math.floor(length/2)):
        index = i * 2 + 1
        sum = sum + int(numStr[index])

    return sum

def sumOdds(numStr):
    '''
    Sums the odd positioned digits of a number
    :param numStr: Number, as a string
    :return: sum of odd position numbers
    '''
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