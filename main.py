import cv2
import os
import numpy as np
import imageio

from matplotlib import pyplot as plt
from PIL import Image

#opencv's video capture is boring...uh

# experiment
# Define the lower and upper bounds for each color to segment
colors = [
    {
        'name': 'red',
        'lower': np.array([0, 50, 50]),
        'upper': np.array([10, 255, 255])
    },
    {
        'name': 'blue',
        'lower': np.array([90, 50, 50]),
        'upper': np.array([130, 255, 255])
    },
]

folder_path = 'data'  # Update with the path to your folder
output_gif = []

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
            mask = cv2.GaussianBlur(mask, (3, 3), 0)
            
            # Perform morphological operations to refine the red mask
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            masks.append(mask)
        #end for

        # Combine the masks to get the segmented regions
        segmented = np.zeros_like(image)

        for mask, color in zip(masks, colors):         
            color_img = cv2.bitwise_and(image, image, mask=mask)
            segmented = cv2.add(segmented, color_img)
        #end for
   
        cv2.imshow('Image', segmented)

        #============================================================
        # Convert the image to HSV color space
        hsv_seg_image = cv2.cvtColor(segmented, cv2.COLOR_BGR2HSV)

        red_mask = cv2.inRange(hsv_seg_image, colors[0]['lower'], colors[0]['upper'])
        blue_mask = cv2.inRange(hsv_seg_image, colors[1]['lower'], colors[1]['upper'])

        # Find contours in the mask
        red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours on the segmented image
        segmented = np.copy(segmented)
        cv2.drawContours(segmented, red_contours, -1, (0, 255, 0), 2)
        cv2.drawContours(segmented, blue_contours, -1, (0, 244, 0), 2)

        # Iterate over the contours and label objects based on color
        for contour in red_contours:
            # Get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Add the label text to the segmented image
            cv2.putText(segmented, 'Robot', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)

        # Iterate over the contours and label objects based on color
        for contour in blue_contours:
            # Get the bounding rectangle of the contour
            x, y, w, h = cv2.boundingRect(contour)

            # Add the label text to the segmented image
            cv2.putText(segmented, 'Blue Object', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)

        # Display or save the result
        cv2.imshow("Segmented Image with Labels", segmented)
        output_gif.append(segmented)
        #=========================================================
        cv2.waitKey(200)
        # end if

    else:
        print(f'Error reading image: {filename}')
    # end else

#end for


# Create a GIF writer object
gif_writer = imageio.get_writer("segmented_images.gif", mode="I", duration=0.5, loop=0)

# Iterate over the segmented images
for segmented_image in output_gif:
    # Convert the segmented image to RGB format
    segmented_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)

    # Add the image to the GIF writer
    gif_writer.append_data(segmented_rgb)

# Close the GIF writer
gif_writer.close()
