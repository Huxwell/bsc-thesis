
	#library used for raspberry camera interface
	from picamera import PiCamera
	#used for storing and processing the camera frames
	from picamera.array import PiRGBArray
	#used for execution time measurements
	import time
	#opencv image processing library
	import cv2 
	#library used for processing images as matrices
	#works faster than Python lists
	import numpy as np 
	#method used for array comprehension operations
	from itertools import izip 
	#used for saving or loading images from storage
	import os 



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
 
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)






dist = 1500
thresh = 170
kernel = 5
par1 = 60
par2 = 25
det_thresh = 1300
dilate_size = 9
offset = 35

def process_frame(frame, thresh, param1, param2, min_radius, max_radius, 
			min_distance, gauss_kernel_size, dilate_kernel_size, detection_threshold):
	#obtaining red channel - 3rd element of tuple returned by split() function:
	red = cv2.split(frame)[2]
	#converting BGR image to HSV scale and obtaining Saturation channel:
	saturation = cv2.split(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))[1] 
	#thresholding with chosen method:
	saturation = cv2.threshold(saturation,thresh,255,cv2.THRESH_BINARY)[1] 
	#gaussian blur for better yolk detection:
	red = cv2.GaussianBlur(red, (gauss_kernel_size,gauss_kernel_size), 0) 
	#detecting yolks with Hough Circles Transform:
	circles = cv2.HoughCircles(red,cv2.HOUGH_GRADIENT,1,min_distance,param1, 
							   param2,minRadius,maxRadius)
	#if circles are found, they are exlcuded from saturation channel:
	if isinstance(circles, np.ndarray): 
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
			#rectangle with offset excluded to delete yellow light reflected from egg yolk:
			cv2.rectangle(saturation,(i[0]-i[2]-offset,0),(i[0]+i[2]+offset,480),0,-2)
	#dilatation and erosion used as image opening to reduce noise:
	saturation = cv2.morphologyEx(saturation, cv2.MORPH_OPEN, 
			cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(dilate_kernel_size,dilate_kernel_size)))
	#summing the remaining egg yolk:
	sum = int(np.sum(saturation)/255) 
	#decision whether or not batch is acceptable:
	return 0 if sum > detection_threshold else 1 
		
		
		
# initialising the camera:
camera = PiCamera()
camera.resolution = (640, 480)
# framerate (frameskipping) that works without delays:
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480))
#warmup time:
time.sleep(0.1)
#grabbing subsequent camera frames:
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	#image.array is a numpy array, the same type that opencv processes:
	frame = image.array
	process_frame(frame, ... ) #values of parameters from Figure 6.4.1 are input here
	#clear the image container:
	rawCapture.truncate(0)		
	
	
	
	
	
	
	
	
	
	
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)		
		
		
		