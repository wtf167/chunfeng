import cv2
import math
import numpy as np
img = cv2.imread("/tmp/dct.bmp",0)
img_water = cv2.imread("/tmp/dct.bmp",0)
print(img.shape)
a, b, c = img.shape
part_a = int(a//8)
part_b = int(b//8)
fingernum = img_water.shape[0] * img_water.shape[1]
r = math.ceil(fingernum/(part_a*part_b))
img = np.float32(img)
finish_pic = img
for i in range(part_a):
    for j in range(part_b):
        part8x8 = cv2.dct(img[8*i:8*i+8, 8*j:8*j+8])
        for t in range(r):
            rx, ry = 4, 4
            r1 = part8x8[rx, ry]
            r2 = part8x8[7-rx, 7-ry]
            detat=abs(r1-r2)
            p = float(detat + 100)
            if img_water[i][j] == 0:
                if r1 <= r2:
                    part8x8[rx, ry] += p
            if img_water[i][j] == 255:
                if r1 >= r2:
                    part8x8[7-rx, 7-ry] += p
        finish_pic[8*i:8*i+8,8*j:8*j+8] = cv2.idct(part8x8)
cv2.imwrite("/tmp/dct2.bmp", finish_pic)