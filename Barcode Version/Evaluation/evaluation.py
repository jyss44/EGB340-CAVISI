import pyzbar.pyzbar as pyzbar
import cv2
import math

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

def evaluateImage(fileName):
    image = cv2.imread(fileName)

    data = decodeImage(image)

    if len(data) > 0:
        print('File', fileName, 'Code detected!')
        print('Code:', data[0])
        return True
    else:
        print('File', fileName, 'No code detected')
        return False

evaluateImage('Test Images/70mmHD.jpg')
evaluateImage('Test Images/90mmHD.jpg')
evaluateImage('Test Images/110mmHD.jpg')
evaluateImage('Test Images/130mmHD.jpg')
evaluateImage('Test Images/150mmHD.jpg')
evaluateImage('Test Images/170mmHD.jpg')
evaluateImage('Test Images/190mmHD.jpg')
evaluateImage('Test Images/210mmHD.jpg')
evaluateImage('Test Images/230mmHD.jpg')
evaluateImage('Test Images/250mmHD.jpg')
evaluateImage('Test Images/270mmHD.jpg')
evaluateImage('Test Images/290mmHD.jpg')

print('Standard definition')
evaluateImage('Test Images/70mmSD.jpg')
evaluateImage('Test Images/90mmSD.jpg')
evaluateImage('Test Images/110mmSD.jpg')
evaluateImage('Test Images/130mmSD.jpg')
evaluateImage('Test Images/150mmSD.jpg')
evaluateImage('Test Images/170mmSD.jpg')
evaluateImage('Test Images/190mmSD.jpg')
evaluateImage('Test Images/210mmSD.jpg')
evaluateImage('Test Images/230mmSD.jpg')
evaluateImage('Test Images/250mmSD.jpg')
evaluateImage('Test Images/270mmSD.jpg')
evaluateImage('Test Images/290mmSD.jpg')

