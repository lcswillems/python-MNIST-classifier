from tensorflow.python.keras.optimizers import SGD, Adam
import numpy

import arguments
import ui
import utils

args = arguments.get_args()

if utils.model_already_exists(args.out):
    model = utils.load_model(args.out)
elif args.mode == "train":
    model = getattr(utils.models, args.model)()
else:
    raise ValueError("Aucun modèle à l'emplacement donné par --out")
model.summary()

if args.mode == "train":
    if args.optimizer == "sgd":
        optimizer = SGD(lr=args.lr)
    elif args.optimizer == "adam":
        optimizer = Adam(lr=args.lr)
    else:
        raise ValueError("Nom d'optimiseur inconnu")

    (x_train, y_train), (_, _) = utils.get_data(num_train_examples=args.examples)

    model.compile(loss="categorical_crossentropy",
                  optimizer=optimizer,
                  metrics=["accuracy"])
    model.fit(x=x_train,
              y=y_train,
              epochs=args.epochs,
              batch_size=128)

    utils.save_model(model, args.out)

elif args.mode == "test":
    (_, _), (x_test, y_test) = utils.get_data()
    cls_test = numpy.argmax(y_test, axis=1)

    y_pred = model.predict(x_test, batch_size=128, verbose=1)
    cls_pred = numpy.argmax(y_pred, axis=1)

    incorrect = (cls_pred != cls_test)

    accuracy = 1 - numpy.mean(incorrect)
    accuracy = round(accuracy*100, 1)
    print("Accuracy: {}%".format(accuracy))

    utils.plot_images(images=x_test[incorrect],
                      cls_true=cls_test[incorrect],
                      cls_pred=cls_pred[incorrect])

elif args.mode == "use":
    ui.build(model)

else:
    raise ValueError("Mode invalide")