import cv2
import os
from matplotlib import pyplot as plt


def main():
    # load image
    folder = "images"
    img_original = cv2.imread(os.path.join(folder, "pneu.png"))

    # get image with only the red channel
    img_red_channel = img_original[:, :, 2]

    # binarize image with otsu method
    _, img_otsu = cv2.threshold(img_red_channel, 0, 255, cv2.THRESH_OTSU)
    # binarize image with fixed threshold
    _, img_otsu = cv2.threshold(img_red_channel, 140, 255, cv2.THRESH_BINARY)

    # create figure
    fig = plt.figure(1)
    plt.set_cmap("gray")

    # Show image 1
    plt.subplot(1, 3, 1)
    plt.title("Original")
    plt.axis("off")
    plt.imshow(img_original)

    # Show image 2
    plt.subplot(1, 3, 2)
    plt.title("Red channel")
    plt.axis("off")
    plt.imshow(img_red_channel)

    # Show image 3
    plt.subplot(1, 3, 3)
    plt.title("Binary")
    plt.axis("off")
    plt.imshow(img_otsu)
    plt.show()

    # get lines' x coordinates
    line1_x1, line1_x2, line2_x1, line2_x2 = find_x_coordinates(img_otsu)
    print(line1_x1, line1_x2, line2_x1, line2_x2)

    # calculate distance from the center of both lines
    distance = (((line1_x1 + line1_x2) / 2) - ((line2_x1 + line2_x2) / 2)) * 0.1
    print("The distance between the centers of both lines is", round(distance, 2), "mm")
    # calculate distance in between both lines
    distance = (line1_x1 - line2_x2) * 0.1
    print("The distance between most right point of line 1 to the most left point of line 2 is",
          round(distance, 2), "mm")


#
# Find the width of two lines in an image
# Returns the 4 x coordinates (start and end of both lines)
#
def find_x_coordinates(img_binary):
    state = 0
    for y in range(img_binary.shape[0]):  # columns
        for x in range(img_binary.shape[1]):  # lines
            # get pixel
            pixel = img_binary[y, x]
            if (state == 0 and pixel == 255):  # first x coordinate of 1st line (start)
                state = 1
                x1 = x
            elif (state == 1 and pixel == 0):  # last x coordinate of 1st line (end)
                state = 2
                x2 = x
            elif (state == 2 and pixel == 255 and x < x1 - 4):  # first x coordinate of 2nd line (start)
                state = 3
                x3 = x
            elif (state == 3 and pixel == 0 and x < x2 - 4):  # last x coordinate of 2nd line (end)
                x4 = x
                return x1, x2, x3, x4


if __name__ == "__main__":
    main()
