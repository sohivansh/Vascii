import cv2 as cv
import numpy as np

def main():

    vid = cv.VideoCapture('assets/test.mp4')
    

    while True:
        ret, frame = vid.read()
        gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        height, width = gray_frame.shape
        gray_frame = cv.resize(gray_frame,(width//4,height//4))
        key = cv.waitKey(1)

        if key == ord('q'):
            break

    vid.release()
    cv.destroyAllWindows()

main()

