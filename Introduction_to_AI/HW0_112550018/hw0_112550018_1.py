import cv2
import os
import numpy as np

image = cv2.imread('image.png')

f = open('bounding_box.txt', 'r')
window_name = 'Image'

for line in f.readlines():
    L = line.split()
    x1, y1, x2, y2 = map(int, L)
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2.imshow(window_name, image)  

f.close()
cv2.imwrite('hw0_112550018.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()