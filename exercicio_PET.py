import cv2
import numpy as np

# read image
image = cv2.imread("PET-Body-02.jpg")
image_float = np.array(image, dtype=np.float32)
image_float = image_float / 255.0
# show original image
cv2.imshow("Original", image)
cv2.waitKey(0)

image_HSV = image_float
# change H value
image_HSV[:, :, 0] = image_float[:, :, 0] * 120 + 240
#image_HSV[:, :, 0] = image_float[:, :, 0] * 240 + 120
# change S value
image_HSV[:, :, 1] = 1
# change V value
image_HSV[:, :, 2] = 1

# convert HSV image to RGB
image_final = cv2.cvtColor(image_HSV, cv2.COLOR_HSV2BGR)
# show manipulated image
cv2.imshow("Final", image_final)
cv2.waitKey(0)
