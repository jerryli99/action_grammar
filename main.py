import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#opencv's video capture is boring...uh

folder_path = 'data'  # Update with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        if image is not None:
            # Process the image (e.g., display, save, etc.)
            cv2.imshow('Image', image)
            cv2.waitKey(0)
        else:
            print(f'Error reading image: {filename}')



"""
img = cv2.imread("image.001.jpg")

channels = cv2.split(img)

cv2.imshow("e", channels[0])
cv2.waitKey()
cv2.imshow("ee", channels[1])
cv2.waitKey()
cv2.imshow("eee", channels[2])
cv2.waitKey()
"""

"""
x = Image.open("image.001.jpg")
print(x.size)
x = cv2.imread("image.001.jpg")
print(x.shape)
x=plt.imread("image.001.jpg")
print(x.shape)
plt.imshow(x)
plt.show()
"""

"""
capture = cv2.VideoCapture("test_video1.mp4")

while True:
    capture.set(cv2.CAP_PROP_FPS, 12)
    ret, frame = capture.read()
    if ret == False:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(500)

capture.release()
cv2.destroyAllWindows()
"""