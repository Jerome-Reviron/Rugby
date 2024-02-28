# Rugby

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Mise en place du projet Django](#MAJ_Projet_Django)

## Introduction <a name="introduction"></a>
Ce répertoire est conçu durant ma formation POEI Développeur Applicatif Python, afin d'intégrer l'entreprise Pharma Pilot à Cournond'Auvergne.<br>
Accompagné par Human Booster et de nombreux intervenants, j'aurai à la suite de cette formation mon premier CDI de reconversion professionnelle Concepteur Développeur d'Applications.

## Installation <a name="installation"></a>
Ce répertoire à été installé durant la formation sur mon compte github personnel et a une visibilité public à des fins de collaborations optimales avec les collaborateurs, intervenants et collègues.

## Utilisation <a name="utilisation"></a>
Ce répertoire se dote d'un fichier "README.md" dans le but de proposer une explication de chaque exercice réaliser durant la formation.<br>
On aura donc dans le sommaire l'ajout permanent des liens vers les exercices avec les consignes et les mise en application des programmes.

## Contribuer <a name="contribuer"></a>
Toutes personnes à une visibilité sur l'entièreté du répertoire. En revanche, aucune modification n'est possible.<br>
Les véritables contributions se font lors de nos échanges en direct ou en visio, durant tout l'apprentissage de cet emploi.<br>
De nombreux cours théoriques et pratiques sont réalisés pour consolider notre culture et employabilité.

## Licence <a name="licence"></a>
Tout droit réservé à moi même, Monsieur Reviron Jérôme.

# Mise en place du projet Django <a name="MAJ_Projet_Django"></a>
Création d’un nouveau repository GitHub.

### Création d’un nouveau repository GitHub
- Démarrez en créant un nouveau repository GitHub. Dans cet exemple, le repository est nommé Pharma_post.
- Créez un nouveau dossier dans le répertoire racine de votre choix.
- Ouvrez le dossier nouvellement créé avec Visual Studio Code.
- Dans le terminal de VS Code, exécutez la commande suivante pour cloner le repository GitHub dans votre dossier local :git clone https://github.com/Jerome-Reviron/Pharma_post.git.
- Fermez Visual Studio Code pour déplacer le fichier .git et le README.md du dossier Pharma_post à la racine du projet.
- Enfin, supprimez le dossier Pharma_post du répertoire.

### Création du fichier Dockerfile à la racine
- Créez un fichier Dockerfile à la racine du projet avec le contenu suivant :<br>
![Dockerfile](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/Dockerfile.png)

### Création du fichier docker-compose.yml à la racine
- Créez un fichier docker-compose.yml à la racine du projet avec un contenu de base.<br>
![docker-compose](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/docker-compose.png)

### Création du fichier requirements.txt à la racine
- Créez un fichier requirements.txt à la racine du projet avec le contenu suivant :<br>
![requirements](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/requirements.png)
- Puis on fait la commande suivante : 
django-admin startproject Pharma_post pour créer un fichier Pharma_post version django.

- Ensuite, on vérifie que l’on se trouve bien sur le bon chemin Immo avec la commande cd Pharma_post, et si on se trouve ici : C:\Users\HB\Desktop\root\ Pharma_post \ Pharma_post > alors on remonte d’un cran avec la commande : cd .. pour être à la racine du dossier Pharma_post.

- Après on crée le dossier app avec la commande : 
python manage.py startapp app.

### Particularités
La calculatrice à 3 boutons présente plusieurs particularités pour améliorer l'expérience utilisateur :

#### Redémarrage de l'Application

À tout moment, l'utilisateur peut choisir de redémarrer l'application en appuyant sur le caractère "R" puis en appuyant sur "valider".<br>
Cela permet de commencer une nouvelle séquence d'opérations sans quitter l'application.

#### Gestion de la Division par Zéro

La calculatrice intègre une protection contre la division par zéro. Si une division par zéro est détectée lors de l'évaluation de l'expression, un message d'erreur est affiché à l'utilisateur.<br>
La calculatrice doit ensuite etre réinitialisée avec le "redémarrer l'application" pour éviter toute incohérence.

#### Désactivation du Clavier

Pour promouvoir une expérience utilisateur centrée sur la souris, l'utilisation du clavier est désactivée pendant l'exécution du programme.<br> 
Cela garantit que l'utilisateur interagit exclusivement avec l'interface graphique de la calculatrice à l'aide de la souris.
