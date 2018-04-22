from tensorflow.python.keras.datasets import mnist
from tensorflow.python.keras.utils import to_categorical

import numpy as np
import scipy as sc

IMG_SIZE = 28
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 1)
IMG_CENTER_SIZE = 20
NUM_CLASSES = 10
NUM_PROCESS_STEPS = 4

def get_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = format_x(x_train)
    x_test = format_x(x_test)

    y_train = format_y(y_train)
    y_test = format_y(y_test)

    return (x_train, y_train), (x_test, y_test)

def format_x(x):
    x = np.array(x)
    x = x.reshape(x.shape[0], IMG_SIZE, IMG_SIZE, 1)
    x = x.astype("float32")
    x /= 255
    return x

def format_y(y):
    y = to_categorical(y, NUM_CLASSES)
    return y

def extract(img):
    if np.any(img):
        img = img.copy()

        while np.sum(img[0]) == 0:
            img = img[1:]

        while np.sum(img[:,0]) == 0:
            img = img[:,1:]

        while np.sum(img[-1]) == 0:
            img = img[:-1]

        while np.sum(img[:,-1]) == 0:
            img = img[:,:-1]
    
    return img

def shrink_center(img):
    rows, cols = img.shape

    if rows > cols:
        factor = IMG_CENTER_SIZE/rows
        rows = IMG_CENTER_SIZE
        cols = round(cols*factor)
    else:
        factor = IMG_CENTER_SIZE/cols
        cols = IMG_CENTER_SIZE
        rows = round(rows*factor)

    img = sc.misc.imresize(img, (rows, cols))

    return img

def fit(img):
    new_img = np.zeros((IMG_SIZE, IMG_SIZE), dtype=img.dtype)

    new_img[:img.shape[0], :img.shape[1]] = img

    return new_img

def recenter(img):
    cy, cx = sc.ndimage.measurements.center_of_mass(img)

    rows, cols = img.shape
    shiftx = np.round(cols/2-cx).astype(int)
    shifty = np.round(rows/2-cy).astype(int)

    img = sc.ndimage.interpolation.shift(img, (shifty, shiftx))

    return img

def binarize(img):
    if np.any(img):
        img = img.copy()

        for j in range(img.shape[1]):
            for i in range(img.shape[0]):
                if img[i][j] >= 50:
                    img[i][j] = 255
                else:
                    img[i][j] = 0
        
    return img

def preprocess(img):
    img1 = extract(img)
    img2 = shrink_center(img1)
    img3 = fit(img2)
    img4 = recenter(img3)
    img5 = binarize(img4)
            
    return img2, img3, img4, img5