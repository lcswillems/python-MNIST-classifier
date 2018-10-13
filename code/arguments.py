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
        help="""Mode d'utilisation du programme : 'train', 'test' ou 'use' (OBLIGATOIRE)
    - train: Entraîne le modèle sur les données d'entraînement
    - test: Teste le modèle sur les données de test
    - use: Utilise le modèle pour classifier de nouveaux chiffres""",
        required=True
    )
    parser.add_argument(
        "--model",
        help="Nom du modèle : 'deepnet1', 'deepnet2', 'convnet' (défaut: deepnet1)",
        default="deepnet1"
    )
    parser.add_argument(
        "--minimizer",
        help="Nom du minimiseur : 'sgd' ou 'adam' (défaut: adam)",
        default="adam"
    )
    parser.add_argument(
        "--epochs",
        help="Nombre d'epochs utilisé par le minimiseur (défaut: 1)",
        type=int,
        default=1
    )
    parser.add_argument(
        "--lr",
        help="Learning rate utilisé par le minimiseur (défaut: 0.0002)",
        type=float,
        default=2e-4
    )
    parser.add_argument(
        "--examples",
        help="Nombre de données utilisées pour l'entraînement (défaut: toutes i.e. 60000)",
        type=int,
        default=None
    )
    parser.add_argument(
        "--batch-size",
        help="(pour les connaisseurs) (défaut: 128)",
        type=int,
        default=128
    )
    return parser.parse_args()