import cv2
import numpy as np

# Load the image
img = cv2.imread("stereoLeft./imageL1.png")

print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('img',gray)
cv2.waitKey(0)
ret, corners = cv2.findChessboardCorners(gray, (7, 7),
                                         flags=cv2.CALIB_CB_ADAPTIVE_THRESH +
                                               cv2.CALIB_CB_FAST_CHECK +
                                               cv2.CALIB_CB_NORMALIZE_IMAGE)
if ret:
    # print(corners)
    fnl = cv2.drawChessboardCorners(img, (7, 7), corners, ret)
    cv2.imshow("fnl", fnl)
    cv2.waitKey(0)
else:
    print("No Checkerboard Found")