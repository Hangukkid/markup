import cv2
import os
import numpy as np
import imutils
from gcloud import detect_handwritten_ocr

MINAREA = 100
XBUFFER = 5
YBUFFER = 5
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
# if not os.path.exists(os.path.join(os.getcwd(), "Answers")):
#     os.makedirs(os.path.join(os.getcwd(), "Answers"))

# if not os.path.exists(os.path.join(os.getcwd(), "TestCases")):
#     os.makedirs(os.path.join(os.getcwd(), "TestCases"))

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
                # print (x, y, w, h)
                x += XBUFFER
                w -= 2*XBUFFER
                y += YBUFFER
                h -= 2*YBUFFER

        return rect, x, y, w, h

def Reformat_Image (ImageFileName, new_size=100):
    image_folder_path = os.path.join(FILE_PATH, "Answers")
    ImageFilePath = os.path.join(image_folder_path, ImageFileName)
    from PIL import Image
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width < new_size and height < new_size):
        background = Image.new('RGBA', (new_size, new_size), (255, 255, 255, 255))
        offset = (int(round(((new_size - width) / 2), 0)), int(round(((new_size - height) / 2),0)))

        background.paste(image, offset)
        background.save(os.path.join(image_folder_path, ImageFileName))
        print("Image has been resized !")

    else:
        print("Image is bigger than necessary")

if __name__ == "__main__":
    #Get all paths
    homeDir = os.getcwd()
    os.chdir(os.path.join(homeDir, "TestCases"))
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

            name = ""
            for c in reversed(cnts):
                rect, x, y, w, h = rd.detect(c)
                if (rect):
                    os.chdir(homeDir)
                    img_crop = img[y:y+h, x:x+w]
                    cv2.imwrite('tempName.png', img_crop)
                    strDet = detect_handwritten_ocr('tempname.png')
                    strDet.split(":") # trying to split and extract "name" using :
                    if (len(strDet) > 1):
                        if (strDet[0] == "name"):
                            name = strDets[1]
                    else:
                        img_name = "Answers/" + name + "(" + str(incr) + ").png"
                        incr += 1
                        cv2.imwrite(img_name, img_crop)

                    os.chdir(curDir)
    # Resizing image if too small
    for image in os.listdir(os.path.join(FILE_PATH, "Answers")):
        Reformat_Image(image, 150)
