import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    # load image
    folder = "images"
    img_original = cv2.imread(os.path.join(folder, "pneu.png"))

    # convert image to grayscale
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    # binarize image with fixed threshold
    _, img_thresh = cv2.threshold(img_gray, 254, 255, cv2.THRESH_BINARY)

    # detect lines using HoughLines method
    lines = cv2.HoughLinesP(img_thresh, rho=1, theta=np.pi/180, threshold=25, minLineLength=50, maxLineGap=50)
    # create copy of original image
    img_lines = img_original.copy()
    # get coordinates of every line detected and draw them on new image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_lines, (x1, y1), (x2, y2), (0, 255, 0), 1)
        cv2.circle(img_lines, (x1, y1), 1, (255, 0, 0), 2)
        cv2.circle(img_lines, (x2, y2), 1, (255, 0, 0), 2)

    # calculate distance
    distance = measure_distance(lines)
    print("The distance between the 2 lines is: {} mm".format(round(distance*0.1, 1)))

    # show resulting images in figure
    plt.set_cmap("gray")
    # show image 1
    plt.subplot(1, 4, 1)
    plt.title("Original")
    plt.axis("off")
    plt.imshow(img_original)

    # show image 2
    plt.subplot(1, 4, 2)
    plt.title("Gray")
    plt.axis("off")
    plt.imshow(img_gray)

    # show image 3
    plt.subplot(1, 4, 3)
    plt.title("Binary")
    plt.axis("off")
    plt.imshow(img_thresh)

    # show image 4
    plt.subplot(1, 4, 4)
    plt.title("Lines")
    plt.axis("off")
    plt.imshow(img_lines)
    plt.show()


def measure_distance(lines):
    # get lines from list
    line1, line2 = lines

    # get points from line1
    x1, y1, x2, y2 = line1[0]
    p1 = np.array([x1, y1])
    p2 = np.array([x2, y2])

    # get points from line2
    x1, y1, x2, y2 = line2[0]
    p3 = np.array([x1, y1])
    p4 = np.array([x2, y2])

    # distance from bottom
    # calculate angle between lines
    angle = get_angle(p1, p3, p4)
    # calculate distance between lines
    h = np.sqrt(((p1[0] - p3[0])**2) + ((p1[1] - p3[1])**2))
    # calculate distance
    distance_bottom = h * np.sin(angle)

    # distance from top
    # calculate angle between lines
    angle = get_angle(p2, p4, p3)
    # calculate distance between lines
    h = np.sqrt(((p2[0] - p4[0])**2) + ((p2[1] - p4[1])**2))
    # calculate distance
    distance_top = h * np.sin(angle)

    # calculate average distance
    distance = np.average([distance_top, distance_bottom])
    return distance


def get_angle(a, b, c):
    # create vectors
    ba = a - b
    bc = c - b

    # calculate angles' cosine value
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    # calculate angle
    angle = np.arccos(cosine_angle)
    return angle


if __name__ == "__main__":
    main()
