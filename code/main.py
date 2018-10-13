from tensorflow.keras.optimizers import SGD, Adam
import numpy

import arguments
import ui
import utils

# Récupère les arguments donnés au programme
args = arguments.get_args()

# Charge le réseau
if utils.model_already_exists(args.out):
    model = utils.load_model(args.out)
elif args.mode == "train":
    model = getattr(utils.models, args.model)()
else:
    raise ValueError("Aucun modèle à l'emplacement donné par --out")

# Affiche une description du réseau : couches, nombres de paramètres
model.summary()

# Instructions exécutées dans le mode 'train'
if args.mode == "train":
    # Charge le minimiseur
    if args.minimizer == "sgd":
        optimizer = SGD(lr=args.lr)
    elif args.minimizer == "adam":
        optimizer = Adam(lr=args.lr)
    else:
        raise ValueError("Nom d'optimiseur inconnu")

    # Charge les données d'entraînement
    x_train, y_train = utils.get_train_data(num_train_examples=args.examples)

    # Entraîne le réseau pendant un certain nombre d'epochs
    model.compile(loss="categorical_crossentropy",
                  optimizer=optimizer,
                  metrics=["accuracy"])
    model.fit(x=x_train,
              y=y_train,
              epochs=args.epochs,
              batch_size=args.batch_size)

    # Enregistre le réseau
    utils.save_model(model, args.out)

# Commandes exécutées dans le mode 'test'
elif args.mode == "test":
    # Charge les données de test
    x_test, y_test = utils.get_test_data()
    cls_test = numpy.argmax(y_test, axis=1)

    # Récupère les prédictions du réseau sur les données
    y_pred = model.predict(x_test, batch_size=128, verbose=1)
    cls_pred = numpy.argmax(y_pred, axis=1)

    # Identifie les prédictions incorrects
    incorrect = (cls_pred != cls_test)

    # Calcule la précision, i.e. le nombre moyen de prédictions correctes
    accuracy = 1 - numpy.mean(incorrect)
    accuracy = round(accuracy*100, 1)
    print("\nAccuracy: {}%".format(accuracy))

    # Propose d'afficher et affiche des exemples d'erreurs
    rep = input("\nAfficher des exemples d'erreurs ? (Y/n)")
    if rep == "" or rep == "Y":
        utils.plot_images(images=x_test[incorrect],
                         cls_true=cls_test[incorrect],
                         cls_pred=cls_pred[incorrect])

# Commandes exécutées dans le mode 'use'
elif args.mode == "use":
    ui.build(model)

else:
    raise ValueError("Mode invalide")