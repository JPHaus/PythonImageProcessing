<<<<<<< HEAD
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

# Save the image
#cv2.imwrite('watchgray.png', img)

# Video processing
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow('Frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
=======
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1

# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

# Save the image
#cv2.imwrite('watchgray.png', img)

# Video processing
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow('Frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
>>>>>>> d79bb5b65e3cba0b7ea4920c75cc7b9e4df34fc3
