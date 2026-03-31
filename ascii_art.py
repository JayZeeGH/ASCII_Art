import cv2
import numpy as np

# ASCII characters from dark to light
ascii_chars = "@%#*+=-:. "

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# ASCII resolution
new_width = 120
new_height = 60

# Font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.3
font_thickness = 1
line_height = 8
char_width = 5

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to ASCII grid
    frame_small = cv2.resize(frame, (new_width, new_height))

    # Convert to grayscale to pick ASCII character based on brightness
    gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)

    # Create blank image for ASCII drawing
    ascii_image = np.zeros((new_height*line_height, new_width*char_width, 3), dtype=np.uint8)

    # Loop through pixels
    for i in range(new_height):
        for j in range(new_width):
            pixel_brightness = gray[i, j]
            brightness_index = int(pixel_brightness) * len(ascii_chars) // 256
            char = ascii_chars[brightness_index]
            
            # Get original color from resized frame
            color = tuple(int(c) for c in frame_small[i, j])  # BGR format

            # Draw character with the original color
            cv2.putText(
                ascii_image,
                char,
                (j*char_width, i*line_height),
                font,
                font_scale,
                color,
                font_thickness,
                lineType=cv2.LINE_AA
            )

    # Show ASCII frame
    cv2.imshow("Colored ASCII Camera", ascii_image)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()