
import cv2
import os
import numpy as np
import imutils

MINAREA = 100

class RectDetector:
    def __init__(self):
        pass

    def detect(self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        rect = False
        x=0
        y=0
        w=0
        h=0
        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            if (w*h > MINAREA):
                rect = True

        return rect, x, y, w, h

if __name__ == "__main__":
    #Get all paths
    homeDir = os.getcwd()
    os.chdir(homeDir + "\TestCases")
    curDir = os.getcwd()

    incr = 0
    #Going through all test images
    for path,dirs,files in os.walk(curDir):
        for filename in files:
            img = cv2.imread(filename)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.bitwise_not(gray, gray)
            blur = cv2.medianBlur(gray, 3)
            blur = cv2.GaussianBlur(blur, (5, 5), 0)
            blur = cv2.bilateralFilter(blur, 9, 75, 75)
            
            thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]

            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            rd = RectDetector()

            
            for c in cnts:
                rect, x, y, w, h = rd.detect(c)
                if (rect):
                    os.chdir(homeDir)
                    img_name = "Answers/" + str(incr) + "(" + str(y) + ").png"
                    incr += 1
                    cv2.imwrite(img_name, img[y:y+h, x:x+w])
                    os.chdir(curDir)
