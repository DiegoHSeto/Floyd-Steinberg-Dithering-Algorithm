import cv2
import numpy as np

path = input("Informe o caminho da imagem: ")

image = cv2.imread(path)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

width, height = grayImage.shape

quantizationFactor = 1

for y in range(0, height-1):
    for x in range(1, width-1):

        oldPixel = grayImage[x][y]

        newPixel = np.round(quantizationFactor * oldPixel/255) * (255/quantizationFactor)

        grayImage[x][y] = newPixel

        quantizationError = oldPixel - newPixel

        grayImage[x+1][y] = grayImage[x+1][y] + quantizationError * 7/16
        grayImage[x-1][y+1] = grayImage[x-1][y+1] + quantizationError * 3/16
        grayImage[x][y+1] = grayImage[x][y+1] + quantizationError * 5/16
        grayImage[x+1][y+1] = grayImage[x+1][y+1] + quantizationError * 1/16


cv2.imshow("Dithered Image", grayImage)
cv2.waitKey()






