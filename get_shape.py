# python get_shape.py -f example.jpg

# import packages
from shapes.detector import Detector
import argparse, imutils, cv2

# get an image
oArgParser = argparse.ArgumentParser()
oArgParser.add_argument("-f", "--file", required=True, help="path to your image")
aInputs = vars(oArgParser.parse_args())

# load and resize the image
image = cv2.imread(aInputs["file"])
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])

# convert to grayscale, blur it slightly, and use threshold
oImageGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
oImageBlurred = cv2.GaussianBlur(oImageGray, (5, 5), 0)
oImageThresh = cv2.threshold(oImageBlurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and use detector
counts = cv2.findContours(oImageThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
counts = counts[0] if imutils.is_cv2() else counts[1]
oShape = Detector()

# loop over the contours
for c in counts:
	# calculate center of the contour, then try to get the name of the shape
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = oShape.detect(c)

	# draw contours and name of the shape
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 2)

	# show the output
	cv2.imshow("Image", image)
    
cv2.waitKey(0)