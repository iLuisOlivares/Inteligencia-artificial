import cv2
import matplotlib.pyplot as plt
import imutils

# mejor modelo hasta ahora
fruit_detector = cv2.CascadeClassifier('cascade/uchuvas/cascade.xml')

ejem_img = cv2.imread("uchuva/Uchuvas8.jpg")
ejem_img = cv2.cvtColor(ejem_img, cv2.COLOR_BGR2RGB)
ejem_img = imutils.resize(ejem_img, width=400, height=400)

print("Pensando...")
fruits = fruit_detector.detectMultiScale(ejem_img, 1.1, 5)
print(fruits)

wa = 0
ha = 0
xa = 0
ya = 0
for i in range(len(fruits)):
    x, y, w, h = fruits[i]
    cv2.rectangle(ejem_img, (x, y), (x+w, y+h), (128, 0, 0), 5)
    if (w > wa):
        wa = w
        ha = h
        ya = y
        xa = x


cv2.rectangle(ejem_img, (xa, ya), (xa+wa, ya+ha), (128, 239, 0), 5)
plt.imshow(ejem_img, cmap='Accent')
plt.show()


# # Prueba de otra versiones
# other_version = cv2.imread("fresas/fresas11.jpg")
# other_version = cv2.cvtColor(other_version, cv2.COLOR_BGR2RGB)
# other_version = imutils.resize(other_version, width=500, height=500)


# fruit_detector = cv2.CascadeClassifier('cascade/fresas/cascade_5.2.xml')

# print("Pensando...")
# fruits = fruit_detector.detectMultiScale(other_version, 1.1, 3)
# print(fruits)

# wa = 0
# ha = 0
# xa = 0
# ya = 0
# for i in range(len(fruits)):
#     x, y, w, h = fruits[i]
#     cv2.rectangle(other_version, (x, y), (x+w, y+h), (128, 0, 0), 5)
#     if (w > wa):
#         wa = w
#         ha = h
#         ya = y
#         xa = x

# cv2.rectangle(other_version, (xa, ya), (xa+wa, ya+ha), (128, 239, 0), 5)
# plt.imshow(other_version, cmap='Accent')
# plt.show()
