# Classifieur Python de chiffres manuscrits

<p align="center"><img src="README-images/demo-ui.gif"></p>

Ce dépôt contient un classifieur de chiffres manuscrits écrit en Python. Il a été réalisé par [Lucas Willems](http://www.lucaswillems.com) pour sa présentation "[Le deep learning pour remplacer les postiers ?](http://seminairespourtous.ens.fr/ipt/1819/exposes/24/le-deep-learning-pour-remplacer-les-postiers)" au séminaire [Info Pour Tous 2018](http://seminairespourtous.ens.fr).

Si jamais vous rencontrez un quelconque problème, vous pouvez ouvrir une nouvelle issue sur [cette page](https://github.com/lcswillems/python-MNIST-classifier/issues) en cliquant sur "New issue".

**Sommaire :**

- [Installation](#installation)
  - [1. Python 3](#1-python-3)
  - [2. Bibliothèques Python](#2-bibliothèques-python)
  - [3. Code du classifieur](#3-code-du-classifieur)
- [Utilisation](#utilisation)
  - [Entraînement du réseau](#entraînement-du-réseau)
  - [Test du réseau](#test-du-réseau)
  - [Utilisation du réseau](#utilisation-du-réseau)
- [Structure du code](#structure-du-code)
  - [Création d'un modèle](#création-dun-modèle)
- [Pour aller plus loin](#pour-aller-plus-loin)

## Installation

Le classifieur requière quelques autres programmes pour fonctionner. Il nous faut donc commencer par les installer.

### 1. Python 3

La première étape de la procédure consiste à installer Python 3, le langage de programmation dans lequel est écrit le classifieur. Voici, pour chaque système d'exploitation, la manière la plus simple de faire :
- pour Windows et Mac, [télécharger Python 3](https://www.python.org/downloads/) puis l'installer. Si jamais vous avez besoin de plus de détails, vous pouvez regarder [cette vidéo Youtube](https://www.youtube.com/watch?v=wp15jyylSEQ).
- pour Linux, ouvrir un terminal puis exécuter `sudo apt update` puis `sudo apt install python3`.

### 2. Bibliothèques Python

La version de base de Python 3 que vous venez d'installer possède beaucoup de fonctionnalités mais ne peut évidemment pas posséder toutes les fonctionnalités imaginables. Or, pour réaliser le classifieur, j'ai eu besoin d'utiliser des fonctionnalités supplémentaires qui ne se trouvent pas dans la version de base. Ces fonctionnalités supplémentaires sont regroupées en ce que l'on appelle des **bibliothèques** ("libraries" en anglais).

6 bibliothèques ont été utilisées pour réaliser le classifieur :

- `tensorflow`: une bibliothèque pour faire du machine learning. Elle permet d'entraîner, tester et utiliser le classifieur.
- `PyQt5`: une bibliothèque pour avoir une interface graphique. Elle permet de dessiner des chiffres dans le mode `use` (voir partie "[Utilisation](#utilisation)" plus bas).
- `matplotlib`: une bibliothèque pour afficher des graphiques, des images... Elle permet d'afficher les erreurs du classifieur dans le mode `test` (voir partie "[Test du réseau](#test-du-réseau)" plus bas).
- `h5py`: une bibliothèque pour manipuler des données. Elle permet de charger et de sauvegarder le classifieur sur votre ordinateur.
- `numpy`: une bibliothèque pour manipuler des tableaux à n dimensions. Elle permet de manipuler facilement les images par exemple.
- `scipy`: une bibliothèque pour faire des calculs scientifiques (statistiques, traitement du signal...). Elle permet d'appliquer certaines transformations sur une image dans le mode `use` (voir partie "[Utilisation](#utilisation)" plus bas).
- `scikit-image`: une bibliothèque pour transformer les images Elle permet d'appliquer certaines transformations sur une image dans le mode `use` (voir partie "[Utilisation](#utilisation)" plus bas).

Actuellement, ces bibliothèques ne se trouvent pas sur votre ordinateur. La deuxième étape de la procédure consiste donc à les télécharger puis les installer. Heureusement, Python inclut déjà un outil, appelé `pip`, permettant de le faire très facilement.

Si vous êtes sous Windows, ouvrez l'invité de commande (tapez "Invité de commande" ou "cmd" dans le menu Démarrer et cliquez sur le programme). Si vous êtes sur Linux ou Mac, ouvrez le terminal. Ensuite, dans tous les cas, exécutez la commande suivante :

```
pip3 install tensorflow pyqt5 matplotlib h5py numpy scipy scikit-image
```

### 3. Code du classifieur

La dernière étape de la procédure consiste à télécharger le code du classifieur. Pour ce faire, cliquez sur le bouton "Clone or download" en haut de [la page du dépôt](https://github.com/lcswillems/python-MNIST-classifier), puis sur "Download ZIP". A la fin du téléchargement, dézippez le fichier.

<p align="center"><img src="README-images/download-code.png"></p>

Voilà, l'installation est terminée ! Vous pouvez dès à présent utiliser le code. La section suivante explique comment faire.

## Utilisation

Pour utiliser le code :
- sous Windows, ouvrez un invité de commande dans ce dossier avec la commande `cd` ([un petit tutoriel](https://www.youtube.com/watch?v=sjaCgavMO18) si besoin). Vous pouvez aussi directement ouvrir l'invité de commande dans le dossier `code` en appuyant sur la touche `shift` puis en faisant clic droit dans le dossier puis sur "Ouvrir une fenêtre de commande ici" ([un petit tutoriel](https://www.howtogeek.com/howto/windows-vista/stupid-geek-tricks-open-a-command-prompt-from-the-desktop-right-click-menu/) si besoin).
- sous Linux ou Mac, ouvrez un terminal et déplacez-vous dans ce dossier avec la commande `cd`.

Dans cet invité de commande / terminal, vous pouvez exécuter des commandes. Par exemple, pour exécuter un programme Python contenu dans le fichier `monfichier.py`, vous pouvez utiliser la commande suivante :

```python3 monfichier.py```

Le seul fichier que vous allez toujours exécuter est `main.py` ("main" veut dire "principal" en français). Les autres fichiers seront seulement utilisés par le fichier `main.py`. Vous pouvez essayer la commande suivante :

```python3 main.py```

Vous devez obtenir l'erreur suivante : `main.py: error: the following arguments are required: --out, --mode`. La raison est que le fichier `main.py` a besoin de recevoir des précisions de l'utilisateur sur ce qu'il doit faire. Ces précisions s'appellent des **arguments**. Certains arguments, dits **optionnels**, ont des valeurs par défaut. Un argument optionnel peut ne pas être spécifié par l'utilisateur, et s'il ne l'est pas, sa valeur par défaut est utilisée par le programme. Certains autres arguments, dits **obligatoires**, n'ont pas de valeur par défaut. Dans ce cas, l'utilisateur doit tout le temps spécifier leurs valeurs.

Dans notre cas, 2 arguments sont obligatoires :
- `--out` : le fichier dans lequel le réseau de neurone est ou doit être enregistré.
- `--mode` : le mode du programme. Il doit valloir soit `train`, soit `test`, soit `use`, c'est-à-dire que le programme doit soit entraîner le réseau de neurones, soit le tester, soit l'utiliser pour classifier des nouveaux chiffres entrés par l'utilisateur. L'utilité de ces modes est développée plus en détail dans les sous-parties suivantes.

Et 6 arguments sont optionnels :
- `--model` : nom du **modèle** (ou classe de généralisation) du réseau de neurones. 3 modèles sont disponibles de base : `deepnet1`, `deepnet2` et `convnet`. Pour ajouter vos propres modèles, lisez [cette sous-partie](#création-dun-modèle).
- ...

La liste de tous les arguments (obligatoires et optionnels) peut être obtenue en exécutant :

```python3 main.py --help```

Voici un exemple de commande :

```python3 main.py --out dn1_lr001 --mode train --model deepnet1 --lr 0.001```

### Entraînement du réseau

Le premier mode d'utilisation du programme est `train`. Il vous permet d'entraîner le réseau de neurones se trouvant dans le fichier donné par `--out`. Si ce fichier n'existe pas, un réseau sera choisi aléatoirement dans le modèle donné par `--model`. De base, 3 modèles de réseaux de neurones sont disponibles : `deepnet1`, `deepnet2` et `convnet`.

Par exemple, si vous souhaitez entraîner un réseau de neurones de modèle `deepnet2`, vous pouvez exécuter :

```python3 main.py --out monreseau --mode train --model deepnet2 --epochs 5```

Lorsque vous exécutez cette commande :

1. Si aucun réseau de neurone ne se trouve dans le fichier donné par `--out`, le programme commence par choisir aléatoirement un réseau dans le modèle donné par `--model`, sinon, il charge le réseau se trouvant dans le fichier.
2. Un descriptif du réseau s'affiche : les différents layers ("couches" en français) et le nombre de paramètres du modèle.
3. Le réseau est entraîné pendant 5 epochs, i.e. le minimiseur change les paramètres du réseau pendant 5 périodes en espérant aboutir à des paramètres donnant une plus petite erreur. L'epoch (le numéro de l'étape), la loss (l'erreur) et l'accuracy (la précision ou taux de bonnes prédictions) sont affichés et mis à jour automatiquement.
4. Le réseau est finalement sauvegardé dans le fichier donné par `--out`.

Une fois la commande précédente exécutée, vous pouvez continuer d'entraîner votre réseau en exécutant de nouveau la commande. Vous n'avez plus besoin de mettre l'argument `--model` et pouvez changer, par exemple, le nombre d'epochs :

```python3 main.py --out monreseau --mode train --epochs 10```

Pendant l'entraînement, l'erreur devrait normalement diminuer et la précision augmenter. Cela signifie que le réseau fait de moins en moins d'erreurs sur les données d'**entraînement**. Au bout d'un certain temps, l'erreur et la précision vont finir par stagner. Cela signifie que le réseau a atteint ses performances maximales sur les données d'entraînement. Avec les valeurs par défaut des arguments, on peut donc facilement trouver dans le modèle `deepnet2` un réseau avec une erreur de 0.015 et une précision de 0.995 après 50 epochs.

Vous pouvez aussi modifier la valeur des autres arguments optionnels pour influencer la vitesse d'apprentissage du réseau. Les valeurs par défaut ne sont pas forcément les "meilleures" valeurs puisqu'elles dépendent du modèle auquel le réseau appartient. Sur le modèle `deepnet2`, vous pouvez essayer de voir l'impact :
- du learning rate en rajoutant `--lr X` où X est un petit nombre (entre 0.1 et 0.00001 typiquement). Sa valeur par défaut est 0.0002. Plus le learning rate est grand, plus les paramètres varient à chaque étape. Si vous prenez 0.001 pour `X`, vous pouvez remarquer que le réseau apprend plus rapidement ! Si vous prenez 0.01 pour `X`, il apprend encore plus rapidement au début, mais l'apprentissage devient vite chaotique : l'erreur augmente, diminue, augmente (elle oscille) et n'arrive pas à descendre en dessous de 0.03. Enfin, si vous prenez 0.1 pour `X`, l'apprentissage est chaotique dès le début. Une stratégie classique à commencer l'entraînement avec un learning rate grand puis à le diminuer progressivement.
- du minimiseur en rajoutant `--minimizer X` où X peut être `sgd` ou `adam`. `sgd` est l'algorithme de la descente de gradient stochastique. `adam` est une version améliorée de `sgd` et est l'algorithme utilisé par défaut : il performe bien mieux que `sgd`. Vous pouvez essayer en rajoutant `--minimizer sgd`.
- du nombre de données utilisées pour l'entraînement en rajoutant `--examples X` où X est le nombre d'exemples d'entraînement pouvant aller de 0 à 60000 (c'est-à-dire tous les exemples d'entraînement).

Maintenant que vous avez bien entraîné le réseau de modèle `deepnet2`, vous pouvez tester son niveau d'apprentissage en suivant les instructions de [la sous-partie suivante](#test-du-modele) ou alors entraîner un réseau d'un autre modèle.

2 autres modèles sont disponibles de base :
- `deepnet1` contient 1 layer dense contrairement à `deepnet2` qui en contient 2. Il est moins performant que ce dernier. Vous pouvez arriver à une erreur de 0.25 et une précision de 0.93 après 50 epochs.
- `convnet` est plus performant que `deepnet2`. Il utilise une certaine opération mathématique appelée **convolution** (vous pouvez lire [cet excellent tutoriel pour débutant](https://adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-Convolutional-Neural-Networks/) pour comprendre et [ce site internet](http://scs.ryerson.ca/~aharley/vis/conv/) pour visualiser). Vous pouvez arriver à une erreur de 0.03 et une précision de 0.99 en 10 epochs.

Notez que l'entraînement de réseaux de `convnet` est beaucoup plus lent !! Commencer avec un grand learning rate (0.01) puis le diminuer progressivement pour arriver à 0.0001 pourra vous économiser beaucoup de temps :
- ```python3 main.py --out monreseau2 --mode train --model convnet --epochs 5 --lr 0.01```
- ```python3 main.py --out monreseau2 --mode train --epochs 20```

### Test du réseau

Une fois que vous avez entraîné votre réseau, il est temps de le tester, de voir s'il est capable de **bien généraliser**. L'erreur et la précision affichées pendant l'entraînement donnent une bonne idée de l'avancement de l'apprentissage du réseau. Mais comme elles sont calculées sur les données d'**entraînement**, elles ne donnent donc aucunement un ordre d'idée de la capacité du réseau à bien généraliser. Pour évaluer cette capacité, il nous faut tester notre réseau, c'est-à-dire regarder sa précision sur des données de test qu'il n'a encore jamais vues.

Pour ce faire, il vous faut utiliser le mode `test` en exécutant, par exemple, la commande suivante :

```python3 main.py --out monreseau --mode test```

La précision sur les données de test s'affiche. Vous pouvez aussi afficher 16 erreurs commises par le réseau.

Normalement, vous devez obtenir les précisions suivantes à quelques choses près :
- 92.6% pour les meilleurs réseaux de `deepnet1`
- 97.8% pour les meilleurs réseaux de `deepnet2`
- 98.8% pour les meilleurs réseaux de `convnet`

Nous pouvons faire deux remarques importantes :
1. Sur les données d'entraînement, les meilleurs réseaux de `deepnet2` ont une précision similaire voire meilleure que ceux de `convnet` alors qu'ils ont une précision nettement inférieure sur les données de test.
2. Les réseaux ont des précisions supérieures sur les données d'entraînement que sur les données de test. On dit qu'ils **sur-interprètent**. Ce phénomène se passe aussi lorsque les humains apprennent : ils sont meilleurs sur des problèmes qu'ils ont déjà vus.

### Utilisation du réseau

Enfin, maintenant que vous avez obtenu un réseau performant, vous pouvez l'utiliser pour classifier de nouveaux chiffres manuscrits, qui ne sont pas dans les données d'entraînement ou de test. Par exemple, vous pouvez l'utiliser pour classifier vos propres chiffres manuscrits.

Pour ce faire, il vous faut utiliser le mode `use` en exécutant, par exemple, la commande suivante :

```python3 main.py --out monreseau --mode use```

Vous pouvez dessiner votre chiffre dans le gros cadre noir. A chaque fois que vous relâchez votre clic, le réseau classifie le chiffre dessiné.

Vous pouvez remarquer 4 petits carrés noirs à droite du gros carré noir dans lesquels le chiffre dessiné apparaît légèrement modifié. Voici plus précisément quelles sont les transformations :
1. Dans le 1er petit carré, la partie noire tout autour du chiffre dessiné a été supprimée puis le chiffre a été redimensionné en conservant les proportions pour qu'il fasse moins 20 pixels de large et 20 pixels de hauteur.
2. Dans le 2e petit carré, des pixels noirs ont été ajoutés en bas et à droite pour que le chiffre fasse exactement 20 pixels de large et 20 pixels de hauteur.
3. Dans le 3e petit carré, le chiffre a été recentré en fonction de son [barycentre](https://fr.wikipedia.org/wiki/Barycentre).

La question que l'on peut se poser est : pourquoi appliquer de telles transformations avant de donner l'image au réseau ? Tout simplement parce que le réseau n'a pas été entraîné et testé sur n'importe quels chiffres manuscrits. Les données d'entraînement et de test étaient normalisées : les chiffres faisaient maximum 20 pixels de large et de hauteur et étaient centrés selon leur barycentre. Pour que le réseau puisse être performant sur les chiffres dessinés par les utilisateurs, il faut aussi appliquer cette transformation (pre-processing).

Enfin, puisque nous venons de parler des transformations appliquées au chiffre dessiné dans le mode `use`, il est temps de vous parler de la transformation magique qui est systématiquement appliquée à une image de chiffre, que ce soit lors de l'entraînement, lors du test ou lors de l'utilisation. Cette transformation est la toute première appliquée et est appelée la **normalisation**. Une image étant un tableau de nombres entre 0 et 255, la normalisation consiste à diviser tous les nombres par 255 pour se retrouver avec un tableau de nombres entre 0 et 1. Normaliser l'image accélère l'apprentissage, mais je ne peux vous expliquer correctement la raison ici malheureusement. Cette transformation va encore rester quelques temps magique pour vous.

## Structure du code

Ce dossier contient :
- `main.py` : fichier principal
- `arguments.py` : fichier où sont définis les arguments de `main.py`
- `models.py` : fichier où sont définis les modèles `deepnet1`, `deepnet2`, `convnet`
- `ui.py` : fichier où est définie l'interface graphique pour le mode `use`
- `utils` : un dossier contenant les fichiers :
    - `data.py` permettant de charger les données et de faire les 4 transformations requises dans le mode `use`
    - `model.py` permettant de charger et de sauvegarder les paramètres d'un réseau de neurones
    - `plot.py` permettant d'afficher des exemples d'erreurs dans le mode `test`
- `storage` : un dossier contenant des sauvegardes des paramètres des différents réseaux

### Création d'un modèle

Si vous voulez créer votre propre modèle `X`, vous devez créer une fonction `X` dans le fichier `models.py`. Voici des idées de modèle que vous pourriez créer :
- Vous pouvez enlever / ajouter des layers au modèle `deepnet2` et diminuer / agrandir la taille des layers.
- Vous pouvez enlever / ajouter plus de layers de convolution au modèle `deepnet2`, enlever les max-pooling, changer la taille des kernels, etc...

Essayez de créer un maximum de modèles, de les entraîner et de voir leur précision pour trouver le modèle qui obtient la plus haute précision.

## Pour aller plus loin

Vous avez fait un bel effort et avez sûrement beaucoup progressé, mais il ne faut pas vous arrêter en si bon chemin !

Le deep learning est un domaine en plein essort depuis ces dernières années, comme j'ai essayé de le montrer à la fin de mon exposé. Par exemple, il est maintenant possible de **transférer le style** d'une image sur une autre (plein d'exemples). Voici un exemple (et plein d'autres [ici](https://github.com/jcjohnson/neural-style)) où à partir du tableau "[La nuit étoilée](https://fr.wikipedia.org/wiki/La_Nuit_%C3%A9toil%C3%A9e)" de Van Gogh et d'une photo du campus de Stanford, le réseau crée une photo du campus de Stanford avec le style de Van Gogh :

<p align="center"><img src="README-images/style-transfer.png"></p>

**Que faire après ?**

Très facilement, vous pouvez tester quelques petits outils pour avoir une meilleure intuition sur le fonctionnement des réseaux de neurones :

- [Tensorflow Playground](https://playground.tensorflow.org/) pour plus vous familiariser avec les réseaux de neurones profonds. Vous pouvez vous amuser à remplacer la fonction ReLU par d'autres fonctions, à changer le learning rate, le nombre de layers, les données, etc...
- [Visualization of ConvNet](http://scs.ryerson.ca/~aharley/vis/conv/) pour plus vous familiariser avec les réseaux de neurones convolutifs.

Mais tester ces petits outils ne vous permettra pas de vraiment maîtriser le deep learning pour obtenir vos premiers résultats.

**Comment devenir un maître du deep learning ?**

3 étapes sont nécessaires selon moi :

1. maîtriser Python;
2. maîtriser la théorie du deep learning;
3. beaucoup pratiquer.

Pour maîtriser Python, vous pouvez suivre le cours "[Apprendre à programmer en Python](https://openclassrooms.com/courses/apprenez-a-programmer-en-python)" de OpenClassrooms qui vous donnera une compréhension complète du langage ou alors le cours "[Programming for everybody](https://www.coursera.org/learn/python)" de Coursera.

Pour maîtriser la théorie, là, malheureusement, ça coince. J'ai beaucoup cherché et n'ai pas réussi à trouver des ressources accessibles au grand public... (si vous en connaissez, donnez les moi !). Pour les personnes ayant un niveau bac+1 en maths, vous pouvez lire "[The Deep Learning Book](https://www.deeplearningbook.org/)" (livre que j'ai lu pour apprendre).

Pour pratiquer, je vous recommende de faire [les TPs confectionnés par Hvass](https://github.com/Hvass-Labs/TensorFlow-Tutorials) qui sont d'une qualité rarissime ! Si vous n'avez pas beaucoup de temps, vous pouvez vous contenter de faire les TPs 1, 2, 3, 4, 5 et 17 qui vous donneront de très bonnes bases avec Tensorflow, et ensuite, de lire les autres TPs attentivement. A travers ces TPs, vous apprendrez entre autre :
- [le transfert de style](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/15_Style_Transfer.ipynb)
- [la traduction de texte](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/21_Machine_Translation.ipynb)
- [les rêves profonds](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/14_DeepDream.ipynb)
- ...

Voilà ! Vous avez de quoi faire ! Bon courage ! Battez-vous, percévérez. Votre travail paiera et vous pourrez rapidement peut-être créer des choses incroyables ! Tenez-moi au courant si vous le pouvez :) .