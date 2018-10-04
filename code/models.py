from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout

import utils

def deepnet1():
    model = Sequential()

    model.add(Flatten(input_shape=utils.IMG_SHAPE))

    model.add(Dense(utils.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model

def deepnet2():
    model = Sequential()

    model.add(Flatten(input_shape=utils.IMG_SHAPE))

    model.add(Dense(128))
    model.add(Activation("relu"))

    model.add(Dense(utils.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model

def convnet():
    model = Sequential()

    model.add(Conv2D(32, kernel_size=(3, 3),
                     input_shape=utils.IMG_SHAPE))
    model.add(Activation("relu"))

    model.add(Conv2D(64, kernel_size=(3, 3)))
    model.add(Activation("relu"))

    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(128))
    model.add(Activation("relu"))

    model.add(Dense(utils.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model