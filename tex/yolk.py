r_c = cv2.GaussianBlur(r, (kernel,kernel), 0)
val,s_c = cv2.threshold(s,thresh,255,cv2.THRESH_BINARY)
circ_no = 0
circles = cv2.HoughCircles(r_c,cv2.HOUGH_GRADIENT,1,dist,param1=par1,
                           param2=par2,minRadius=90,maxRadius=230)