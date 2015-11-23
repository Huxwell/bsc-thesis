for param1 in xrange(10,80,5):
    for param2 in xrange(10,90,5):
        for kernel_size in xrange(1,30,2):
            for offset in (5,80,5):
                # ...
                grade_frame(detect_yolks(frame))