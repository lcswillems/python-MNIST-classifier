from argparse import ArgumentParser, RawTextHelpFormatter

def get_args():
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "--out",
        help="Nom du fichier dans lequel le modèle est sauvegardé (OBLIGATOIRE)",
        required=True
    )
    parser.add_argument(
        "--mode",
        help="""Mode d'utilisation : 'train', 'test' ou 'use' (OBLIGATOIRE)
    - train: Entraîne le modèle sur les données d'entraînement
    - test: Teste le modèle sur les données de test
    - use: Utilise le modèle pour classifier de nouveaux chiffres""",
        required=True
    )
    parser.add_argument(
        "--model",
        help="Nom du modèle (ou classe de généralisations) (défaut: deepnet1)",
        default="deepnet1"
    )
    parser.add_argument(
        "--epochs",
        help="Nombre d'entraînement du modèle sur toutes les données d'entraînement (défaut: 1)",
        type=int,
        default=1
    )
    parser.add_argument(
        "--optimizer",
        help="Nom de l'optimiseur pour entraîner le modèle : 'sgd' ou 'adam' (défaut: adam)",
        default="adam"
    )
    parser.add_argument(
        "--lr",
        help="Learning rate utilisé par l'optimiseur (défaut: 0.0002)",
        type=float,
        default=2e-4
    )
    parser.add_argument(
        "--batch-size",
        help="Nombre d'exemples utilisés pour chaque minimisation (défaut: 128)",
        type=int,
        default=128
    )
    parser.add_argument(
        "--examples",
        help="Nombre de données d'entraînement (défaut: toutes i.e. 60000)",
        type=int,
        default=None
    )
    return parser.parse_args()