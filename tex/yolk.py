def detect_yolks(frame):
    b,g,r = cv2.split(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ...
    # 'c' variable - channel is chosen among the above
    c = cv2.GaussianBlur(c, (kernel,kernel), 0)
    c = cv2.threshold(c,threshold,255,thresholding_method)
    circles = cv2.HoughCircles(c,cv2.HOUGH_GRADIENT,1,dist,param1,
                               param2,minRadius,maxRadius)
    return circles