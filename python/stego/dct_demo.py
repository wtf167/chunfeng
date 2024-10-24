import numpy as np
import cv2
import math

img = np.float32(cv2.imread("/tmp/dct.bmp", 1))
print(img)
fingernum = img.shape[0] * img.shape[1]
r = math.ceil(fingernum//(64*64))
print(r)
for i in range(64):
    for j in range(64):
        for k in range(3):
            imgg=img[:, :, k]
            dctt = cv2.dct(imgg[8*i:8*i+8, 8*j:8*j+8])
            if (dctt[7,7] >= 10):
                print('1',end='')
            elif(dctt[7,7] < -10):
                print('0',end='')