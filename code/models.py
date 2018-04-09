from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout

import data

def linear():
    model = Sequential()
    model.add(Flatten(input_shape=data.IMG_SHAPE))

    model.add(Dense(data.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model

def mlp():
    model = Sequential()
    model.add(Flatten(input_shape=data.IMG_SHAPE))

    model.add(Dense(128))
    model.add(Activation("relu"))

    model.add(Dense(data.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model

def cnn():
    model = Sequential()

    model.add(Conv2D(32, kernel_size=(3, 3),
                     input_shape=data.IMG_SHAPE))
    model.add(Activation("relu"))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(128))
    model.add(Activation("relu"))

    model.add(Dense(data.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model