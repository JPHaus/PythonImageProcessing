import numpy as np
import cv2

img = cv2.imread('bookspine.jpg', cv2.IMREAD_COLOR)
edges = cv2.Canny(img, 100, 100) 

cv2.imshow('original', img)
cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows