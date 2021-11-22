import cv2
import numpy as np

# read image
image = cv2.imread("cao.jpg")
image_float = np.array(image, dtype=np.float32)
image_float = image_float / 255.0
# show original image
cv2.imshow("Original", image_float)
cv2.waitKey(0)

# convert original image to HSV
image_HSV = cv2.cvtColor(image_float, cv2.COLOR_BGR2HSV)

# change H value to blue
image_HSV[:, :, 0] = 120.0

# convert HSV image to RGB
image_HSV_BGR = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)
# show manipulated image
cv2.imshow("Final", image_HSV_BGR)
cv2.waitKey(0)
