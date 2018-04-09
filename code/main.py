#!/usr/bin/env python3

from tensorflow.python import keras
from tensorflow.python.keras.optimizers import SGD, Adam
from tensorflow.python.keras.callbacks import TensorBoard

import arguments
import data
import models
import ui

def load_model(name):
    try:
        global MODEL_LOCATION

        MODEL_LOCATION = "storage/" + name + ".h5"
        return keras.models.load_model(MODEL_LOCATION)
    except OSError:
        return getattr(models, name)()

def save_model(model):
    def create_file_if_not_exists(file_location):
        import os

        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "w"):
            pass

    global MODEL_LOCATION

    create_file_if_not_exists(MODEL_LOCATION)
    keras.models.save_model(model, MODEL_LOCATION)

def train_model(model, optimizer, epochs):
    (x_train, y_train), (_, _) = data.get()

    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])

    model.fit(x=x_train,
              y=y_train,
              epochs=epochs,
              batch_size=128)
    
    save_model(model)

def test_model(model):
    (_, _), (x_test, y_test) = data.get()

    score = model.evaluate(x_test, y_test, batch_size=128)
    print("Accuracy: {}%".format(round(score[1]*100, 1)))

def use_model(model):
    ui.build(model)

args = arguments.get_args()
assert int(args.train) + int(args.test) + int(args.use) == 1

model = load_model(args.model)

if args.train:
    lr = 1e-4 if args.lr == None else args.lr
    optimizer = Adam(lr=lr) if args.optimizer == "adam" else SGD(lr=lr)
    train_model(model, optimizer, args.epochs)

elif args.test:
    test_model(model)

elif args.use:
    use_model(model)