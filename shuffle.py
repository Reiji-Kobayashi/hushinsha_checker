
import os
import glob
import random
import shutil

dir = input('select_dir: ')
files = glob.glob('./' + dir + '/*.jpg')

trcount=0
tecount=0


for f in files:
    if(random.random()>=0.2 and trcount<270):
        shutil.move("./"+f, "./train_dataset")
        trcount=trcount+1
    elif(tecount <30):
        shutil.move("./"+f, "./test_dataset")
        tecount=tecount+1
