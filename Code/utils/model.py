import os
from tensorflow import keras

import models
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def get_model_path(out):
    return os.path.join("storage", out + ".h5")

def model_already_exists(out):
    path = get_model_path(out)
    return os.path.isfile(path)

def load_model(out):
    path = get_model_path(out)
    return keras.models.load_model(path)

def save_model(model, name):
    path = os.path.join("storage", name + ".h5")
    keras.models.save_model(model, path)