import os
import cv2
import pytesseract

tesseract_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Read image
folder = "images"
img = cv2.imread(os.path.join(folder, "ui_001.jpg"))
cv2.imshow("Original image", img)

# Convert to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img_gray)

# Binarize image
_, img_tresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image", img_tresh)

# Find biggest counter (screen)
contours, hierarchy = cv2.findContours(img_tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
big_contour = max(contours, key=cv2.contourArea)
# Get bounding box around screen
x, y, w, h = cv2.boundingRect(big_contour)

# Create mask image
mask = img.copy() * 0
mask = cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)
cv2.imshow("Mask", mask)

# Multiply gray image with screen mask
img_screen = cv2.bitwise_and(img, mask)
cv2.imshow("Screen image", img_screen)

# Convert to gray scale
img_screen_gray = cv2.cvtColor(img_screen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray screen", img_screen_gray)

# Binarize and invert image
_, img_result = cv2.threshold(img_screen_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_BINARY_INV)
cv2.imshow("Result image", img_result)
cv2.waitKey(0)

# Get text from image
text = pytesseract.image_to_string(img_result)
print('Text length:', len(text))

if text:
    print("Text: ")
    print(text)

    # Process text
    text_array = text.split()
    if len(text_array) >= 4:
        room = text_array[0] + text_array[1]
        hours = text_array[2]
        password = text_array[-1]

        print(text_array)
        print(room)
        print(hours)
        print(password)
    else:
        print("Couldn't find enough words")
