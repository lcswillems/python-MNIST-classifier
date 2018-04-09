from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "--model",
        help="Nom du modèle",
        required=True
    )
    parser.add_argument(
        "--train",
        help="Entraine le modèle sur les données d'entraînement",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "--epochs",
        help="Nombre de passages sur les données d'entraînement pour entrainer le modèle",
        default=1,
        type=int
    )
    parser.add_argument(
        "--optimizer",
        help="Optimiseur",
        default="adam"
    )
    parser.add_argument(
        "--lr",
        help="Learning rate utilisé par l'optimiseur",
        default=None,
        type=float
    )
    parser.add_argument(
        "--test",
        help="Teste le modèle sur les données de test",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "--use",
        help="Utilise le modèle pour classifier de nouveaux chiffres",
        action="store_true",
        default=False
    )
    return parser.parse_args()