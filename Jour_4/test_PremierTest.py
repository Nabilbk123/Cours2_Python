### 1: Installer "pytest" => pip install pytest
### 2: Creer un fichier python => Doit contenir le mot "test" au début
### 3: Importer le package "pytest"
### 4: creer des fonctions "pytest"=>  Elles doivent commencer par "test" (Rappel:  Pour creer les fcts ont utilise: "def"
### 5: Pour executer les tests on doit aller dans le dossier des tests et on execute la commande suivante :
###### pytest test_PremierTest.py  -s -v ( "-s":Pour afficher le contenu en forme de caractéres & "-v":Pour afficher plus de contenu)


import pytest

def test_login():
    print("Ce connecter sur google")

def test_creerCompte():
    print("Creer un compte google")