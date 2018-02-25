# import openCV
import cv2

class Detector:
	def __init__(self):
		pass

	def detect(self, c):
		shape = "Unbekannt"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		# 3 vertices => triangle
		if len(approx) == 3:
			shape = "Dreieck"
            

		# 4 vertices => square or rectangle
		elif len(approx) == 4:
			# use the bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# square => aspect ratio that is approximately equal to one, 
            # otherwise, the shape is a rectangle
			shape = "Quadrat" if ar >= 0.95 and ar <= 1.05 else "Rechteck"

		# 5 vertices => pentagon
		elif len(approx) == 5:
			shape = "Pentagon"

		# otherwise, we assume the shape is a circle# 5 vertices => pentagon
		elif len(approx) >8 :
			shape = "TODO"

		# otherwise => circle		
		else:
			shape = "Kreis"

		return shape