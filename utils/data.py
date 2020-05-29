from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy
import scipy
import skimage
import skimage.transform

IMG_SIZE = 28
IMG_SHAPE = (IMG_SIZE, IMG_SIZE)
IMG_CENTER_SIZE = 20
NUM_CLASSES = 10
NUM_PROCESS_STEPS = 4

def get_train_data(num_train_examples=None):
    (x_train, y_train), _ = mnist.load_data()
    if num_train_examples != None:
        x_train = x_train[:num_train_examples]
        y_train = y_train[:num_train_examples]

    x_train = format_x(x_train)
    y_train = format_y(y_train)

    return x_train, y_train

def get_test_data():
    _, (x_test, y_test) = mnist.load_data()

    x_test = format_x(x_test)
    y_test = format_y(y_test)

    return x_test, y_test

def format_x(x):
    x = numpy.array(x)
    x = x.astype("float32")
    x /= 255
    return x

def format_y(y):
    y = to_categorical(y, NUM_CLASSES)
    return y

def extract(img):
    if numpy.any(img):
        img = img.copy()

        while numpy.sum(img[0]) == 0:
            img = img[1:]

        while numpy.sum(img[:,0]) == 0:
            img = img[:,1:]

        while numpy.sum(img[-1]) == 0:
            img = img[:-1]

        while numpy.sum(img[:,-1]) == 0:
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

    img = img.astype(float) / 255
    img = skimage.transform.resize(img, (rows, cols), anti_aliasing=True, mode='constant')
    img = (img * 255).astype(int)

    return img

def fit(img):
    new_img = numpy.zeros(IMG_SHAPE, dtype=img.dtype)

    new_img[:img.shape[0], :img.shape[1]] = img

    return new_img

def recenter(img):
    cy, cx = scipy.ndimage.measurements.center_of_mass(img)

    rows, cols = img.shape
    shiftx = numpy.round(cols/2-cx).astype(int)
    shifty = numpy.round(rows/2-cy).astype(int)

    img = scipy.ndimage.interpolation.shift(img, (shifty, shiftx))

    return img

def preprocess(img):
    img1 = extract(img)
    img2 = shrink_center(img1)
    img3 = fit(img2)
    img4 = recenter(img3)

    return img2, img3, img4
