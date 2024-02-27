import cv2
import os
import numpy as np

video = cv2.VideoCapture('video.mp4')
if not video.isOpened:
    print("Video is not opened")
    exit()

while True:
    ret1, frame1 = video.read()
    ret2, frame2 = video.read()
    frame4 = frame2
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame3 = cv2.absdiff(frame1, frame2)
    frame3 = cv2.cvtColor(frame3, cv2.COLOR_GRAY2BGR)
    t, frame3 = cv2.threshold(frame3, 30, 255, cv2.THRESH_BINARY)
    stack_frame = np.hstack((frame4, frame3))
    cv2.namedWindow("video",0)
    cv2.resizeWindow("video",1200,450)
    cv2.imshow('video', stack_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

video.release()

