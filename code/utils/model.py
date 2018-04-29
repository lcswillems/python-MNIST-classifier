import os
from tensorflow.python import keras

import models

def load_model(name):
    try:
        path = os.path.join("storage", name + ".h5")
        return keras.models.load_model(path)
    except OSError:
        return getattr(models, name)()

def save_model(model, name):
    path = os.path.join("storage", name + ".h5")
    keras.models.save_model(model, path)