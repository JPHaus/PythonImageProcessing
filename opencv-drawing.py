import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# image, start coords, end coords, color (BGR), line width
cv2.line(img, (0,0), (150,150), (255,255,255), 15)
cv2.rectangle(img, (15,25), (200,150), (0, 255, 0), 5)

# image, center of circle, radius, color, negative fills in space
cv2.circle(img, (100,63), 55, (0,0,255), -1)

# polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()