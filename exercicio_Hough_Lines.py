import cv2
import os
import numpy as np

# load image
folder = "images"
img_original = cv2.imread(os.path.join(folder, "pneu.png"))

# get image with only the red channel
img_red_channel = img_original[:, :, 2]

# binarize image with fixed threshold
_, img_thresh = cv2.threshold(img_red_channel, 254, 255, cv2.THRESH_BINARY)

# detect edges
edges = cv2.Canny(img_thresh, 50, 150)
cv2.imshow("Edges (Canny)", edges)

rho = 1
theta = np.pi/180
threshold = 1

def update_lines():
    lines = cv2.HoughLinesP(edges, rho=rho, theta=theta, threshold=threshold, minLineLength=50, maxLineGap=50)
    img_lines = img_original.copy()
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_lines, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("Lines", img_lines)

def on_trackbar_rho(val):
    global rho
    rho = val
    update_lines()

def on_trackbar_threshold(val):
    global threshold
    threshold = val
    update_lines()

cv2.namedWindow("Lines")
cv2.createTrackbar("rho", "Lines", rho, 100, on_trackbar_rho)
cv2.createTrackbar("threshold", "Lines", threshold, 100, on_trackbar_threshold)
update_lines()
cv2.waitKey(0)
