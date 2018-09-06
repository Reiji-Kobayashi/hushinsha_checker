import numpy as np
import tensorflow as tf
from load_dataset import load_dataset
import matplotlib.pyplot as plt

from PIL import Image


def analyse(imagename):
    #iname = input("filename: ")
    #im = Image.open(iname+".jpg", "r")

    # 入力変数
    x = tf.placeholder(tf.float32, shape=[None, 64*64*3])
    y_ = tf.placeholder(tf.float32, shape=[None, 2])
    W = tf.Variable(tf.zeros([64*64*3,2]))
    b = tf.Variable(tf.zeros([2]))

    #  出力層
    y = tf.matmul(x,W) + b
    p = tf.nn.softmax(y)

    #モデル読み込み
    saver = tf.train.Saver()
    sess=tf.InteractiveSession()
    saver.restore(sess, "./model/sample_model")

    img = np.frombuffer(np.array(Image.open(imagename).convert('RGB')),dtype=np.uint8)
    img = img.astype(np.float32)
    # 正規化
    img /= 255.0
    predict_img = np.array([img])
    ans = np.argmax(sess.run(p,feed_dict={x:predict_img}))

    if(ans == 0):
        #print('hushin')
        return 1
    elif(ans == 1):
        #print('anzen')
        return 0
