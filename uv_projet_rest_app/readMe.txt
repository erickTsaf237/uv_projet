# Application Flask avec API REST

Cette application est composée d'une API REST développée avec Flask et d'une application front-end.

## Installation

1. utiliser l'environnement de base de anaconda



2. Installez les dépendances à partir du fichier `requirements.txt` :
    lancer la coomande pip install -r requirements.txt


## Structure du projet

L'application est organisée comme suit :

- `uv_project_rest_app/` : Contient le code de l'API REST Flask ainsi que la vue
  - `__init__.py` : Initialise l'application Flask
  - `resources.py` : Définit les ressources de l'API REST
  - `models.py` : Définit les modèles de données SQLAlchemy
  - `view/` : Contient le code de l'application front-end
- `notebooks/` : Contient les notebooks Jupyter utilisés pour le développement et l'analyse des données

## Modèles de données

Les modèles de données sont définis dans les notebooks Jupyter situés à la racine du projet.

## Lancement de l'application

1. Assurez-vous que l'environnement est completement installee
2. Lancez l'application Flask : cela se fait juste en executant le main
3. Ouvrez la page html, elle est vide, Ouvrez l'inspecteur et comencez a tapper dans le cham de saisie