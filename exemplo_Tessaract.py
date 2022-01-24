import cv2
import os
import pytesseract
from matplotlib import pyplot as plt

tesseract_path = "C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = tesseract_path

folder = "images"
img = cv2.imread(os.path.join(folder, "texto.jpg"))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_tresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)


# subplot 1
plt.subplot(3, 1, 1)
plt.title("Original")
plt.axis("off")
plt.imshow(img)

# subplot 2
plt.subplot(3, 1, 2)
plt.title("Gray")
plt.axis("off")
plt.imshow(img_gray)

# subplot 3
plt.subplot(3, 1, 3)
plt.title("Threshold")
plt.axis("off")
plt.set_cmap("gray")
plt.imshow(img_tresh)

# print result on figure
text = pytesseract.image_to_string(img_tresh)
plt.text(img.shape[1]/3, 110, text)
plt.show()

cv2.waitKey(0)
