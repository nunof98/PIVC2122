import cv2
import os
import numpy as np

folder = "images"
img = cv2.imread(os.path.join(folder, "moedas.jpg"))

window_name = "Moedas original"
cv2.namedWindow(window_name)
cv2.imshow("Moedas original", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

canny_tresh_min = 150
canny_tresh_max = 200
edges = cv2.Canny(img_gray, canny_tresh_min, canny_tresh_max)


def on_trackbar_canny_min(val):
    global canny_tresh_min, edges
    canny_tresh_min = val
    edges = cv2.Canny(img_gray, canny_tresh_min, canny_tresh_max)
    cv2.imshow("Moedas Canny", edges)


def on_trackbar_canny_max(val):
    global canny_tresh_max, edges
    canny_tresh_max = val
    edges = cv2.Canny(img_gray, canny_tresh_min, canny_tresh_max)
    cv2.imshow("Moedas Canny", edges)


cv2.namedWindow("Moedas Canny")
cv2.createTrackbar("canny_tresh_min", "Moedas Canny", canny_tresh_min, 255, on_trackbar_canny_min)
cv2.createTrackbar("canny_tresh_max", "Moedas Canny", canny_tresh_max, 255, on_trackbar_canny_max)
cv2.imshow("Moedas Canny", edges)

dp = 1
minDist = 20
param1 = 50
param2 = 50

def update_circles():
    circles = cv2.HoughCircles(edges, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2)
    circles = circles[0]

    img_with_circles = img.copy()
    for circle in circles:
        cv2.circle(img_with_circles, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
    cv2.imshow("Moedas circulos", img_with_circles)

def on_trackbar_dp(val):
    global dp
    dp = val
    update_circles()

def on_trackbar_minDist(val):
    global minDist
    minDist = val
    update_circles()

def on_trackbar_param1(val):
    global param1
    param1 = val
    update_circles()

def on_trackbar_param2(val):
    global param2
    param2 = val
    update_circles()

cv2.namedWindow("Moedas circulos")
cv2.createTrackbar("dp", "Moedas circulos", dp, 10, on_trackbar_dp)
cv2.createTrackbar("minDist", "Moedas circulos", minDist, 20, on_trackbar_minDist)
cv2.createTrackbar("param1", "Moedas circulos", param1, 100, on_trackbar_param1)
cv2.createTrackbar("param2", "Moedas circulos", param2, 100, on_trackbar_param2)
update_circles()

cv2.waitKey(0)
