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
cv2.createTrackbar("canny_tresh_min", "Moedas Canny", canny_tresh_min, 1024, on_trackbar_canny_min)
cv2.createTrackbar("canny_tresh_max", "Moedas Canny", canny_tresh_max, 1024, on_trackbar_canny_max)
cv2.imshow("Moedas Canny", edges)

img_gray = img_gray/255.0

Mx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]], dtype=np.float64)

My = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]], dtype=np.float64)

dx = cv2.filter2D(img_gray, -1, kernel=Mx)
cv2.imshow("dx", dx)

dy = cv2.filter2D(img_gray, -1, kernel=My)
cv2.imshow("dy", dy)

gradient = np.sqrt(dx**2 + dy**2)
cv2.imshow("Gradiente", gradient)

th = 200/300.0
_, thresholded_gradient = cv2.threshold(gradient, th, 255, 0)


def on_trackbar_th(val):
    global th
    th = val / 100.0
    _, thresholded_gradient = cv2.threshold(gradient, th, 255, 0)
    cv2.imshow("Moedas Gradient", thresholded_gradient)


cv2.namedWindow("Moedas Gradient")
cv2.createTrackbar("th", "Moedas Gradient", int(th*300), 300, on_trackbar_th)

cv2.waitKey(0)
