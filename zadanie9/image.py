import imutils
import cv2
from cv2 import cv2
image = cv2.imread("soccer.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

cv2.imshow("Image", image)
cv2.waitKey(0)

(B, G, R) = image[182, 50]
print("R={}, G={}, B={}".format(R, G, B))

roi = image[60:160, 140:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
resized = cv2.resize(image, (140, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

output = image.copy()
cv2.putText(output, "OpenCV + Ball!!!", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)