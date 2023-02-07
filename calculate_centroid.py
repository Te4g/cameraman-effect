import cv2

# Load the image
image = cv2.imread('image.jpg')

# Get image dimensions
image_height, image_width, _ = image.shape

sumX = 0
sumY = 0
nbItems = 0

# Open the file in read mode
with open('/Users/gaetan/Ngtv/poc-yolov/yolov7/runs/detect/exp34/labels/input_25.txt', 'r') as file:
    # Iterate over the lines in the file
    for line in file:
        # Strip leading and trailing whitespace from the line
        line = line.strip()

        # Split the line into columns
        cols = line.split()

        # Convert the columns to floats
        cols = [float(col) for col in cols]


        # Get the x-coordinate, y-coordinate, width, and height from the columns
        x, y = cols[1], cols[2]

        if y > 0.7:
            continue

        sumX += x
        sumY += y
        nbItems += 1

avg_x = sumX / nbItems
avg_y = sumY / nbItems


# Get image dimensions
image_height, image_width, _ = image.shape

# Calculate the x-coordinate and y-coordinate of the centroid in pixels
centroid_x = int(avg_x * image_width)
centroid_y = int(avg_y * image_height)

# Calculate the dimensions of the cropped image in pixels
cropped_width = 720
cropped_height = 406

# Calculate top-left and bottom-right coordinates of the cropped image
top_left_x = centroid_x - cropped_width // 2
top_left_y = centroid_y - cropped_height // 2
bottom_right_x = centroid_x + cropped_width // 2
bottom_right_y = centroid_y + cropped_height // 2

# Crop the image
cropped_image = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

# Save the cropped image
cv2.imwrite('cropped_image.jpg', cropped_image)