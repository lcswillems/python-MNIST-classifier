#!/usr/bin/env python3

from tensorflow.python.keras.optimizers import SGD, Adam
import numpy as np

import arguments
import ui
import utils

args = arguments.get_args()

model = utils.load_model(args.model)
model.summary()

if args.mode == "train":
    if args.optimizer == "sgd":
        optimizer = SGD(lr=args.lr)
    elif args.optimizer == "adam":
        optimizer = Adam(lr=args.lr)
    else:
        raise ValueError("Nom d'optimiseur inconnu")

    (x_train, y_train), (_, _) = utils.get_data()

    model.compile(loss="categorical_crossentropy",
                  optimizer=optimizer,
                  metrics=["accuracy"])
    model.fit(x=x_train,
              y=y_train,
              epochs=args.epochs,
              batch_size=128)
    
    utils.save_model(model, args.model)

elif args.mode == "test":
    (_, _), (x_test, y_test) = utils.get_data()
    cls_test = np.argmax(y_test, axis=1)

    y_pred = model.predict(x_test, batch_size=128, verbose=1)
    cls_pred = np.argmax(y_pred, axis=1)

    incorrect = (cls_pred != cls_test)

    accuracy = 1 - np.mean(incorrect)
    accuracy = round(accuracy*100, 1)
    print("Accuracy: {}%".format(accuracy))

    utils.plot_images(images=x_test[incorrect],
                      cls_true=cls_test[incorrect],
                      cls_pred=cls_pred[incorrect])

elif args.mode == "use":
    ui.build(model)

else:
    raise ValueError("Mode invalide")