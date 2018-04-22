from argparse import ArgumentParser, RawTextHelpFormatter

def get_args():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "--mode",
        help="""Mode d'utilisation : 'train', 'test' ou 'use' (REQUIRED)
    - train: Entraîne le modèle sur les données d'entraînement
    - test: Teste le modèle sur les données de test
    - use: Utilise le modèle pour classifier de nouveaux chiffres""",
        required=True
    )
    parser.add_argument(
        "--model",
        help="Nom du modèle (REQUIRED)",
        required=True
    )
    parser.add_argument(
        "--epochs",
        help="Nombre d'entraînement du modèle sur toutes les données d'entraînement (default: 1)",
        type=int,
        default=1
    )
    parser.add_argument(
        "--optimizer",
        help="Nom de l'optimiseur pour entraîner le modèle : 'sgd' ou 'adam' (default: adam)",
        default="adam"
    )
    parser.add_argument(
        "--lr",
        help="Taux d'apprentissage utilisé par l'optimiseur (default: 0.0002)",
        type=float,
        default=2e-4
    )
    return parser.parse_args()