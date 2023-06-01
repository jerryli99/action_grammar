import cv2
import os
import types
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#opencv's video capture is boring...uh
# Define the lower and upper bounds for each color you want to segment
colors = [
    {
        'name': 'red',
        'lower': np.array([0, 50, 50]),
        'upper': np.array([10, 255, 255])
    },
    {
        'name': 'blue',
        'lower': np.array([90, 50, 70]),
        'upper': np.array([128, 255, 255])
    },
    {
        'name': 'gray',
        'lower': np.array([0, 0, 40]),
        'upper': np.array([180, 18, 230])
    }
]


folder_path = 'data'  # Update with the path to your folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #end if

    if image is not None:
        # Process the image (e.g., display, save, etc.)
        masks = []
        for color in colors:
            mask = cv2.inRange(hsv_img, color['lower'], color['upper'])
            masks.append(mask)
        #end for

        # Combine the masks to get the segmented regions
        segmented = np.zeros_like(image)
        for mask, color in zip(masks, colors):
            color_img = cv2.bitwise_and(image, image, mask=mask)
            segmented = cv2.add(segmented, color_img)
        #end for

        cv2.imshow('Image', segmented)
        cv2.waitKey(200)
    # end if

    else:
        print(f'Error reading image: {filename}')
    # end else

#end for
