import cv2
import numpy as np
im = cv2.imread('l4t4.png')
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)
kernel = np.ones((5, 5), np.uint8)
cv2.waitKey(0)