def grade_frame(frame, circles):
    b,g,r = cv2.split(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ...
    # 'c' variable - channel is chosen among the above
    if isinstance(circles, np.ndarray):
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.rectangle(s_c,(i[0]-i[2]-offset,0),(i[0]+i[2]+offset,frame.height),0,-2)
    ellipse = cv2.MORPH_ELLIPSE,(kernel_size,kernel_size)]
    kernel = cv2.getStructuringElement(ellipse)
    c = cv2.morphologyEx(c, morphology_type, kernel)
    sum = np.sum(c)
    return 0 if sum > detction_threshold else 1