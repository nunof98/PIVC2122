import os
import cv2
import numpy as np

folder = "images"
img = cv2.imread(os.path.join(folder, "qr_code.png"))
cv2.imshow("QR Code", img)

qrDecoder = cv2.QRCodeDetector()

data, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)

# Data
print(data)

# Bounding Box
p1 = bbox[0]
p2 = bbox[2]
p1 = p1[0]
p2 = p2[0]

img_bbox = cv2.rectangle(img, (p1[0], p1[1]), (p2[0], p2[1]), (0, 255, 0), thickness=2)
cv2.imshow("Bounding box", img_bbox)

# Rectified Image
rectifiedImage = np.uint8(rectifiedImage)
cv2.imshow("Rectified Image", rectifiedImage)

cv2.waitKey(0)
