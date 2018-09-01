from trimming import trim
import glob
from makedata import reshape
from train import act
import os
import shutil
import cv2


def main_act():
    #print(response)
    fileName = "./inputs/sample.jpg"
    print(fileName)

    capture = cv2.VideoCapture(3)
    ret, image = capture.read()
    if ret == True:
        cv2.imwrite(fileName, image)

    trim()
    reshape()

    files = glob.glob('./outputs/*.jpg')
    result = 0

    for f in files:
        result = result + act(f)

    if(result!=0):
        print("通報！！！！！！！！！！！！")
    else:
        print("not通報")

    files = glob.glob('./outputs/*.jpg')
    for f in files:
        os.remove(f)

#files = glob.glob('./outputs/*.jpg')
#for f in files:
#    os.remove("./inputs/*")
