from trimming import trim
import glob
from makedata import reshape
from analyse import analyse
from trains import trains
import os
import shutil
import cv2


def main_act():
    #print(response)
    fileName = "./inputs/sample.jpg"
    print(fileName)

    capture = cv2.VideoCapture(1)
    ret, image = capture.read()
    if ret == True:
        cv2.imwrite(fileName, image)

    trim()
    reshape()

    files = glob.glob('./outputs/*.jpg')
    result = 0

    for f in files:
        result = result + analyse(f)

    if(result!=0):
        print()
        print("通報！！！！！！！！！！！！")
        print()
        return 1;
    else:
        print()
        print("not通報")
        print()
        return 0;

    files = glob.glob('./outputs/*.jpg')
    for f in files:
        os.remove(f)

    files = glob.glob('./outputs/*.jpg')
    for f in files:
        os.remove("./inputs/*")
