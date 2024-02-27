import numpy as np
import cv2
import os

image = cv2.imread('image.png')

# rotate
rotated = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('rotated.png',rotated)

#crop
x = 100#座標
y = 100

w = 250#裁切長寬
h = 200

cropped = image[y:y+w,x:x+w]
cv2.imwrite('cropped.png',cropped)

#flipping
flipped = cv2.flip(image, 1)
cv2.imwrite('flipped.png',flipped)

#scaling
scaled = cv2.resize(image, (512, 256), interpolation=cv2.INTER_AREA)
cv2.imwrite('scaled.png', scaled)

#translation
height, width = image.shape[:2]
q_height, q_width = height/4 , width/4
T = np.float32([[2,0, q_width], [0,1,q_height]])

translated = cv2.warpAffine(image, T, (width,height))
cv2.imwrite('translated.png', translated)

cv2.waitKey(0)
cv2.destroyAllWindows()