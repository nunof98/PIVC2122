import cv2
import os
import numpy as np

folder = "images"
img = cv2.imread(os.path.join(folder, "Sharbat_Gula.jpg"))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

harris_corners = cv2.cornerHarris(img_gray, blockSize=2, ksize=3, k=0.04)
img_harris = img.copy()
img_harris[harris_corners > 0.01 * harris_corners.max()] = [0, 255, 0]
cv2.imshow("Harris corners", img_harris)

#sift = cv2.SIFT_create()
#sift_kp, sift_desc = sift.detectAndCompute(img, None)
#img_sift = img.copy()
#img_sift = cv2.drawKeypoints(img_gray, sift_kp, None)
#cv2.imshow("Image SIFT", img_sift)

#surf = cv2.xfeatures2d.SURF_create()
#surf_kp, surf_desc = surf.detectAndCompute(img, None)
#img_surf = img.copy()
#img_surf = cv2.drawKeypoints(img_gray, surf_kp, None)
#cv2.imshow("Image SURF", img_surf)

orb = cv2.ORB_create()
orb_kp, surf_desc = orb.detectAndCompute(img, None)
img_orb = img.copy()
img_orb = cv2.drawKeypoints(img_gray, orb_kp, None)
cv2.imshow("Image ORB", img_orb)

cv2.waitKey(0)
