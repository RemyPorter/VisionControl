"""Construct a set of recognizers by looking in the data folder for images."""

import numpy as np
import cv2
import os
import sys

root, _ = os.path.split(sys.modules[__name__].__file__)

basepath = os.path.join(root, "data")

def images(prefix=basepath):
    loadpath = os.path.join(basepath,"images")
    for f in os.listdir(loadpath):
        path = os.path.join(loadpath, f)
        yield path

def descriptions(prefix=basepath):
    orb = cv2.ORB_create()
    for p in images():
        i = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
        keypoints,descriptors = orb.detectAndCompute(i, None)
        rootfile, _ = os.path.splitext(p)
        rootfile = rootfile.replace("images","descriptors")
        rootfile += ".npy"
        np.save(rootfile, descriptors)

def load_descriptors(prefix=basepath):
    loadpath = os.path.join(basepath, "descriptors")
    return [np.load(os.path.join(loadpath, f))
        for f in os.listdir(loadpath) if f.endswith(".npy")]