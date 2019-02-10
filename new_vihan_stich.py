from Stitcher import stitcher
# import the necessary packages
import argparse
import imutils
import cv2
frame1 = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic1.jpg')
frame2 = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic2.jpg')
#while True:
	#flag, frame = cap.read()
	#cv2.imwrite(r'C:\Users\PIYUSH\Desktop\pic2.jpg',frame)
	#frame2=cv2.imread(r'C:\Users\PIYUSH\Desktop\pic2.jpg')

	# load the two images and resize them to have a width of 400 pixels
	# (for faster processing)
	#imageA = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic1.jpg')
	#imageB = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic2.jpg')
frame1 = imutils.resize(frame1, width=400)
frame2 = imutils.resize(frame2, width=400)

	# stitch the images together to create a panorama
stitcher = stitcher()
(result, vis) = stitcher.stitch([frame1, frame2], showMatches=True)
	#frame1=frame2
	# show the images
	#cv2.imshow("Image A", imageA)
cv2.imshow("stiched",vis)

cv2.waitKey(0)
	#v2.imshow("Keypoint Matches",vis)
	#cv2.imshow("Result", result)
	#if cv2.waitKey(10) & 0xFF == ord('q'):
	#	break
