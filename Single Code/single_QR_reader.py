import zbar
import cv2

reader = zbar.Scanner()

img = cv2.imread('../QR Stickers/Bread.png')

results = reader.scan(img)