import cv2
import os
import imutils

input_images_path = "input_images"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "/home/sebastian/Documents/FruitDetector/output_images"
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)

count = 0
for file_name in files_names:

    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        continue

    image = imutils.resize(image, width=38, height=38)

    cv2.imwrite(output_images_path + "/image" + str(count) + ".jpg", image)
    count += 1
