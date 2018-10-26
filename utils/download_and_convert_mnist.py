#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os


def conv_mnist(img_file,label_file, num, path, list,label):

    imgs = open(img_file, "rb").read()
    imgs = np.fromstring(imgs, dtype=np.uint8)
    imgs = imgs[16:]
    imgs = imgs.reshape((num, 28, 28))

    labels = open(label_file,"rb").read()
    labels = np.fromstring(labels, dtype=np.uint8)
    labels = labels[8:] # skip header

    fw = open(list, "w")
    for i in range(num):
        class_id = labels[i]
        img_name = "%s_%05d_c%d.png" % (label, i, class_id)
        img_path = path + "/" + img_name
        cv2.imwrite(img_path, imgs[i])
        fw.write(img_path + "\n")
    fw.close()


data_files = ["train-images-idx3-ubyte.gz",
              "train-labels-idx1-ubyte.gz",
              "t10k-images-idx3-ubyte.gz",
              "t10k-labels-idx1-ubyte.gz"]

cwd = os.getcwd()
for data_file in data_files:
    data_path = cwd + "/data/" + data_file
    if not os.path.exists(data_path):
        os.system('curl -O {} http://yann.lecun.com/exdb/mnist/'.format(data_path, data_file))
        os.system('gunzip ' + data_file)

mnist_folder = cwd + "/data/mnist"
img_path = cwd + "/data/mnist/images"

if not os.path.exists(img_path):
    if not os.path.exists(mnist_folder):
        os.mkdir(mnist_folder)
    os.mkdir(img_path)

conv_mnist("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte", 10000, img_path, "mnist.valid.list","v")
conv_mnist("train-images-idx3-ubyte", "train-labels-idx1-ubyte", 60000, img_path, "mnist.train.list","t")