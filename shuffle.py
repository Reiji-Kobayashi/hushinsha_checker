
import os
import glob
import random
import shutil

dir = input('select_dir: ')
files = glob.glob('./' + dir + '/*.jpg')

for f in files:
    if(random.random()>=0.25):
        shutil.move("./"+f, "./train")
    else:
        shutil.move("./"+f, "./test")
