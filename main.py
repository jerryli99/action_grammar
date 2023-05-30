import cv2
import os
import types
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#opencv's video capture is boring...uh

folder_path = 'data'  # Update with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        #pixel = image[220, 450] # [y, x]
        #print(pixel)
        (img_width, img_height, img_dim) = image.shape
        for i in range (0, img_width, 80):
            for j in range (0, img_height, 80):
                cv2.imshow('', image[i:i+80, j:j+80])
                cv2.waitKey(500)
                
        break
        if image is not None:
            # Process the image (e.g., display, save, etc.)
            cv2.imshow('Image', image)
            cv2.waitKey(1)
        else:
            print(f'Error reading image: {filename}')


