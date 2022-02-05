import os
import cv2
import numpy as np

# Read image
folder = "images"
img = cv2.imread(os.path.join(folder, "baboon.png"))
cv2.imshow("Original image", img)

# Convert to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", img_gray)

# Normalize image in float
img_float = img_gray / 255.0

fft = np.fft.fft2(img_float)
# fft to visualize
fft_v = np.abs(fft) / np.mean(np.mean(np.abs(fft)))
cv2.imshow("FFT", fft_v)

fft_shift = np.fft.fftshift(fft)
# fft_shift to visualize
fft_shift_v = np.abs(fft_shift) / np.mean(np.mean(np.abs(fft_shift)))
cv2.imshow("FFT_shift", fft_shift_v)

shape = fft_shift.shape
H_lowpass = np.zeros(shape)
H_highpass = np.ones(shape)
radius_max = shape[0] / 2
radius = 0.5 * radius_max
center_y = shape[0] / 2
center_x = shape[1] / 2

for y in range(shape[0]):
    for x in range(shape[1]):
        d = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        if d < radius:
            H_lowpass[y, x] = 1
            H_highpass[y, x] = 0

cv2.imshow("H_lowpass", H_lowpass)
cv2.imshow("H_highpass", H_highpass)

fft_shift_filtered = fft_shift * H_lowpass
# fft_shift_filtered to visualize
fft_shift_filtered_v = np.abs(fft_shift_filtered) / np.mean(np.mean(np.abs(fft_shift_filtered)))
cv2.imshow("FFT_shit filtered", fft_shift_filtered_v)

fft_shift_filtered_unshift = np.fft.ifftshift(fft_shift_filtered)
# fft_shift_filtered_unshift to visualize
fft_shift_filtered_unshift_v = np.abs(fft_shift_filtered_unshift) / np.mean(np.mean(np.abs(fft_shift_filtered_unshift)))
cv2.imshow("FFT_shit filtered unshift", fft_shift_filtered_unshift_v)

fft_shift_filtered_unshift_ifft = np.fft.ifft2(fft_shift_filtered_unshift)
fft_shift_filtered_unshift_ifft = np.abs(fft_shift_filtered_unshift_ifft)
cv2.imshow("FFT_shit filtered unshift ifft", fft_shift_filtered_unshift_ifft)

cv2.waitKey(0)
