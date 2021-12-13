import numpy as np
from cv2 import cv2 as cv2

def convolucao(image, kernel):
    (H, W) = image.shape
    offset = (int)(np.floor(kernel.shape[0]/2))
    img_expanded = np.zeros((H+2*offset, W+2*offset))
    print(img_expanded.shape)
    img_expanded[1:img_expanded.shape[0]-1, 1:img_expanded.shape[1]-1] = image
    img_expanded[0, 1:img_expanded.shape[1]-1] = img_expanded[1, 1:img_expanded.shape[1]-1]
    img_expanded[-1, 1:img_expanded.shape[1]-1] = img_expanded[-2, 1:img_expanded.shape[1]-1]
    img_expanded[1:img_expanded.shape[0]-1, 0] = img_expanded[1:img_expanded.shape[0]-1, 1]
    img_expanded[1:img_expanded.shape[0]-1, -1] = img_expanded[1:img_expanded.shape[0]-1, -2]
    img_expanded[0, 0] = img_expanded[1,1]
    img_expanded[0, -1] = img_expanded[1, -2]
    img_expanded[-1, 0] = img_expanded[-2, 1]
    img_expanded[-1, -1] = img_expanded[-2, -2]
    result = np.zeros(image.shape)
    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            v = 0
            for ky in range(kernel.shape[0]):
                for kx in range(kernel.shape[1]):
                    kv = kernel[ky, kx]
                    pixel = img_expanded[y+ky, x+kx]
                    v = v + kv * pixel
            result[y, x] = v
    return result


img = cv2.imread("cao.jpg", 0)
img = img / 255.0
cv2.imshow("original", img)

# filtro = np.ones((3, 3), dtype="float32")
filtro = [ [0, -1, 0],
           [-1, 4, -1],
           [0, -1, 0] ]
filtro = [ [1/9, 1/9, 1/9],
           [1/9, 1/9, 1/9],
           [1/9, 1/9, 1/9] ]
filtro = np.array(filtro)
imagem_filtrada2 = cv2.filter2D(img, -1, kernel=filtro)
cv2.imshow("resultado2", imagem_filtrada2)

imagem_filtrada = convolucao(img, filtro)
cv2.imshow("resultado", imagem_filtrada)
cv2.waitKey(0)
print("end")