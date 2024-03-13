import cv2 
import numpy as np

imagen = cv2.imread('MonedaNXQ.jpg')

scale_percent = 20 
width = int(imagen.shape[1] * scale_percent/100)
heigth = int(imagen.shape[0] * scale_percent/100)
dim = (width, heigth)

resized = cv2.resize(imagen, dim, interpolation = cv2.INTER_AREA)

print('Resized dimensions: ', resized.shape)
cv2.imshow('Resized image', resized)
cv2.waitKey(0)

grises = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
#_,th = cv2.threshold(grises,178,255, cv2.THRESH_BINARY_INV)
grises2 = cv2.GaussianBlur(grises,(7,7), 2)
cv2.imshow('Escala de grises', grises2)
cv2.waitKey(0)

canny = cv2.Canny(grises2, 50, 160)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Mostrar contornos
print('Encontre {} objetos'.format(len(contornos)))

cv2.drawContours(resized ,contornos, -1, (0,0,255),2)
cv2.imshow('Contornos', resized)
cv2.waitKey(0)

#Mayor contorno
Areas = []

for i in contornos:
    Circ = cv2.contourArea(i)
    Areas.append(Circ)

print("Areas: ",str(Areas))

cien = 0
docientos = 0
quinientos = 0
mil = 0

for m in Areas:
    if m >=4300 and m <=5000:
        print("100 Pesos")
        cien = cien + 1
    
    if m >=6100 and m <=6630:
        print("500 Pesos")
        quinientos = quinientos + 1
    
    if m >=6700 and m <= 7300:
        print("200 Pesos")
        docientos = docientos + 1
    
    if m >=7700 and m <=9000:
        print("1000 Pesos")
        mil = mil + 1

SumTotal = cien*100 + docientos*200 + quinientos*500 + mil*1000

print("En la imagen hay $ ", str(SumTotal))

#cv2.imshow('th', th)
cv2.waitKey(0)
cv2.destroyAllWindows()