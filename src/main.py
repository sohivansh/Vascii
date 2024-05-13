import cv2 as cv
import numpy as np

def main():

    vid = cv.VideoCapture('assets/test.mp4')

    while True:
        ret, frame = vid.read()
        new_frame = cv.resize(frame,(1200,1200))
        new_frame = cv.resize(new_frame,(0,0),fx=0.5,fy=0.5)
        for i in new_frame.height:
            for j in vid.get(4):
                average = (new_frame[i][j][0]+new_frame[i][j][1]+new_frame[i][j][2])//3

        

            
        
        cv.imshow('Video',new_frame)


        key = cv.waitKey(1) 
        if key == ord('q'):
            break

    vid.release()
    cv.destroyAllWindows()

main()

