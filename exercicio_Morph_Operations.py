import cv2
import os
import numpy as np

# load image in grayscale
folder = "images"
img_gray = cv2.imread(os.path.join(folder, "moedas.jpg"), cv2.IMREAD_GRAYSCALE)
cv2.imshow("Moedas Original", img_gray)

# binarize image with fixed threshold
_, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("Moedas Thresh", img_thresh)

# dilate image
kernel = np.ones((3, 3), dtype=np.uint8)
img_dilated = cv2.dilate(img_thresh, kernel)
cv2.imshow("Dilated", img_dilated)

# erode image
img_eroded = cv2.erode(img_dilated, kernel)
cv2.imshow("Eroded", img_eroded)

# segmented image
mask = np.uint8(img_eroded / 255)
img_segmented = img_gray * mask
cv2.imshow("Segmented image", img_segmented)
cv2.waitKey(0)
