from tensorflow.python import keras

import models

def load_model(name):
    try:
        return keras.models.load_model("storage/" + name + ".h5")
    except OSError:
        return getattr(models, name)()

def save_model(model, name):
    keras.models.save_model(model, "storage/" + name + ".h5")