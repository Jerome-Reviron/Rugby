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

### Commandes pour créer le projet Django
1. Exécutez la commande suivante pour créer un projet Django nommé Pharma_post : django-admin startproject Pharma_post
2. Vérifiez que vous êtes dans le bon répertoire avec la commande : cd Pharma_post
3. Si vous vous trouvez dans le répertoire : C:\Users\HB\Desktop\root\Pharma_post\Pharma_post >
4. Sinon remontez d'un cran avec la commande : cd ..
5. Ensuite, créez le dossier "app" avec la commande : python manage.py startapp app

### Commandes GitHub
1. Ajoutez tous les fichiers au suivi de Git : git add .
2. Effectuez un premier commit : git commit -m "Initial commit"
3. Poussez les changements vers la branche principale (main) : git push origin main
4. Créez une nouvelle branche "dev" : git checkout -b dev
5. Ajoutez et committez les modifications sur la branche "dev" : git add . et git commit -m "first commit on dev branch"
6. Poussez les changements vers la branche "dev" : git push origin dev

### Commande Docker

1. docker-compose build
2. docker-compose up
3. python manage.py makemigrations
4. python manage.py migrate

#### Commande settings.py

![settings_path](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/settings_path.png)<br>
![settings_installed_app](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/settings_installed_app.png)<br>
![settings_root_templates](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/settings_root_templates.png)<br>
![settings_databases](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/settings_databases.png)<br>
![settings_static](https://github.com/Jerome-Reviron/Rugby/blob/main/images_documentation/settings_static.png)<br>
