
import os
import glob
from PIL import Image

def reshape():
#dir = input('select_dir: ')
    files = glob.glob('./outputs/*.jpg')

    for f in files:
        img = Image.open(f)
        img_resizeimg_resize = img.resize((64, 64))
        img_resizeimg_resize = img_resizeimg_resize.convert('L')
        ftitle, fext =  os.path.splitext(f)
        img_resizeimg_resize.save(ftitle + fext)
