import numpy as np
import cv2

a = np.ndarray((704, 576), dtype=np.uint8)
a[0:, 0:] = 127

a[0:10, :] = 0  # first row
a[-10:, :] = 0  # last row
#s = a.shape
#a[s[0]-10:s[0], :] = 0

a[:, 0:10] = 0  # first column
a[:, -10:] = 0  # last column


cv2.imshow("Imagem", a)
cv2.waitKey(0)
