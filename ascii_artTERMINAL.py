#first prototype
#ascii art program
#import libs
import cv2
import numpy as np
import os

#define ascii characters
ascii_characters = "@%#*+=-:. "


#open camera
cap = cv2.VideoCapture(0)

#start loop
while True: 
#capture frame
    ret, frame = cap.read()
    if not ret:
        break
#convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#resize frame
    gray = cv2.resize(gray, (120,60))
#map pixel values to ascii characters
    ascii_image = ""
    for row in gray:
        for pixel in row:
            ascii_image += ascii_characters[int(pixel) * len(ascii_characters) // 256]
        ascii_image += "\n"
            
    os.system("cls" if os.name == "nt" else "clear")
#display ascii art
    print(ascii_image)
#exit on key press
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()