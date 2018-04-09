# Classifieur Python de chiffres manuscrits

<p align="center"><img src="README-images/demo-ui.gif"></p>

Ce dépôt contient un classifieur de chiffres manuscrits écrit en Python. Il a été réalisé par [Lucas Willems](http://www.lucaswillems.com) pour [sa présentation "Lecture automatique de codes postaux"](http://seminairespourtous.ens.fr) au séminaire [Info Pour Tous 2018](http://seminairespourtous.ens.fr).

- [Installation](#installation)
    - [1. Python 3](#1-python-3)
    - [2. Paquets Python](#2-paquets-python)
    - [3. Code du classifieur](#3-code-du-classifieur)
- [Utilisation](#utilisation)
    - [Entraînement du modèle](#entra%C3%AEnement-du-mod%C3%A8le)
    - [Test du modèle](#test-du-mod%C3%A8le)
    - [Utilisation du modèle](#utilisation-du-mod%C3%A8le)
- [Structure du code](#structure-du-code)
- [Pour aller plus loin](#pour-aller-plus-loin)

## Installation

Avant de pouvoir utiliser le classifieur, vous devez installer les programmes requis.

### 1. Python 3

La première étape de la procédure consiste à télécharger puis installer [Python 3](https://www.python.org/downloads/), le langage de programmation dans lequel le classifieur est écrit. Si jamais vous avez besoin de plus de détails pour y arriver, vous pouvez regarder [cette vidéo Youtube](https://www.youtube.com/watch?v=wp15jyylSEQ).

### 2. Paquets Python

La version de base de Python 3 que vous venez d'installer possède beaucoup de fonctionnalités mais ne peut évidemment pas posséder toutes les fonctionnalités imaginables. Or, pour réaliser le classifieur, j'ai utilisé des fonctionnalités supplémentaires qui ne se trouvent pas dans la version de base. Ces fonctionnalités supplémentaires sont regroupées en ce que l'on appelle des paquets (packages en anglais).

4 paquets ont été utilisés pour réaliser le classifieur :

- `numpy` et `scipy` : deux paquets pour faire des calculs scientifiques. Plus précisément, ces paquets offrent des fonctionnalités pour manipuler les tableaux et les matrices, pour faire des statistiques, du traitement du signal...
- `tensorflow`: un paquet pour faire de l'apprentissage automatique. C'est grâce à ce paquet que le classifieur fonctionne.
- `PyQt5`: un paquet pour avoir une interface graphique. C'est grâce à ce paquet qui permet de dessiner des chiffres.

Actuellement, ces paquets ne se trouvent pas sur votre ordinateur. La deuxième étape de la procédure consiste donc à les télécharger puis les installer. Heureusement, Python inclut déjà un outil, appelé `pip`, permettant de le faire très facilement.

Si vous êtes sous Windows, ouvrez l'invité de commande (tapez "Invité de commande" ou "cmd" dans le menu Démarrer et cliquez sur le programme). Si vous êtes sur Linux ou Mac OS, ouvrez le terminal. Ensuite, dans tous les cas, exécutez la commande suivante :

```
python3 -m pip install numpy scipy tensorflow pyqt5
```

### 3. Code du classifieur

La dernière étape de la procédure consiste à télécharger le code du classifieur. Pour ce faire, cliquez sur le bouton "Clone or download" en haut de [la page du dépôt](https://github.com/lcswillems/python-MNIST-classifier), puis sur "Download ZIP". A la fin du téléchargement, dézippez le fichier.

<p align="center"><img src="README-images/download-code.png"></p>

Voilà, l'installation est terminée ! Vous pouvez dès à présent utiliser le code. La section suivante explique comment faire.

## Utilisation

### Entraînement du modèle

### Test du modèle

### Utilisation du modèle

## Structure du code

## Pour aller plus loin