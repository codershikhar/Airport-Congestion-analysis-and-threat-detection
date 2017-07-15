import time
import numpy as np
import cv2
file_name = '1.MP4'
image = np.fromfile(file_name, dtype ='uint8')
def readImagePlane(row,col,level,offset,final):
    global image
    start = time.time()
    final = np.zeros(shape = (row,col), dtype = np.uint8)

    i = 0

    for m in range(row):
        for n in range(col):
            final[m,n] = image[level*row*col*3 + i + offset]
            i = i + 1
    end = time.time()
    print(end-start)
    return final

readImagePlane(0,0,)