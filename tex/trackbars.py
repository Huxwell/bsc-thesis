cv2.createTrackbar('source', 'Egg', 3, 4, nothing)
cv2.createTrackbar('threshold', 'Egg', 176, 255, nothing)
cv2.createTrackbar('thr_type', 'Egg', 1, 2, nothing)
cv2.createTrackbar('gauss_kernel_size', 'Egg', 10, 30, nothing)
cv2.createTrackbar('minDist', 'Egg', 100, 500, nothing)
cv2.createTrackbar('param1', 'Egg', 50, 150, nothing)
cv2.createTrackbar('param2', 'Egg', 30, 100, nothing)
# ...
param2 = cv2.getTrackbarPos('param2', 'Egg')
# ...