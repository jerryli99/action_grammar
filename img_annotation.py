import cv2
import os

image = cv2.imread('train_red_block_data\Image.001.png')

# Create a window to display the image
cv2.namedWindow('Image')

# Annotation variables
annotations = []
start_point = None
end_point = None
is_drawing = False

# Mouse callback function
def annotate_image(event, x, y, flags, param):
    global start_point, end_point, is_drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        # Set the starting point of the rectangle
        start_point = (x, y)
        is_drawing = True

    elif event == cv2.EVENT_LBUTTONUP:
        # Set the ending point of the rectangle
        end_point = (x, y)
        is_drawing = False

        # Draw the rectangle on the image
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow('Image', image)

        # Add the annotation to the list
        annotations.append((start_point, end_point))

# Register the mouse callback function
cv2.setMouseCallback('Image', annotate_image)

# Display the image
cv2.imshow('Image', image)

# Wait for the user to annotate the image
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the annotations or use them in further processing
# Save the annotated images
output_dir = 'annotated_images'
os.makedirs(output_dir, exist_ok=True)

for i, annotation in enumerate(annotations):
    start_point, end_point = annotation

    # Create a copy of the image with the annotated rectangle
    annotated_image = image.copy()
    cv2.rectangle(annotated_image, start_point, end_point, (0, 255, 0), 2)

    # Save the annotated image to the output directory
    output_path = os.path.join(output_dir, f"image.{i}.png")
    cv2.imwrite(output_path, annotated_image)

    print(f"Annotated image {i+1} saved to {output_path}")


print("Annotations:")
for annotation in annotations:
    print(f"Start Point: {annotation[0]}")
    print(f"End Point: {annotation[1]}")