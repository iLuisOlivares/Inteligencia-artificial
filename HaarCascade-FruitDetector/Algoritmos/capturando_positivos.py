import cv2
import numpy as np
import imutils
import os

Datos = "positive-images"
if not os.path.exists(Datos):
    print("Carpeta creada: ", Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(0, cv2.CAP_V4L)

x1, y1 = 190, 80
x2, y2 = 450, 398
# cap.set(3, 640)  # width
# cap.set(4, 480)  # height
# cap.set(10, 100)  # brightness
count = 0

while True:
    success, frame = cap.read()
    if success == False:
        break

    inAux = frame.copy()
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    objecto = inAux[y1:y2, x1:x2]
    objecto = imutils.resize(objecto, width=38, height=38)
    cv2.imshow('frame', frame)
    cv2.imshow('object', objecto)

    k = cv2.waitKey(1)

    if k == 27:
        break

    if k == ord('s'):
        cv2.imwrite(Datos + '/objeto_{}.jpg'.format(count), objecto)
        print("Imagen almacenada:", "objecto:{}.jpg".format(count))
        count = count + 1


cap.release()
cv2.destroyAllWindows()
