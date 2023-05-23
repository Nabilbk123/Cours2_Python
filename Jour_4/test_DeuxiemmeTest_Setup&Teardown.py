"""

   L'utilisation des prés-conditions (setup) et des post-conditions (teardown)

1 : Ouverture & fermeture du navigateur se repete dans chaque tests
    A eviter (dry - Dont.Repeat.Yourself)
    Pour eviter cela : Il faut creer deux fonctions (instructions / setup & teardown) qui seront repetées une seule fois a chaque test   :Cela permettra d'eviter la repetition du code et d'optimiser sa performance
    ainsi que la maintenance de celui ci

"""

import pytest

### le module: est la suite de tests / le fichier python dans le quel nous avons ecris nos tests
### Le parametre (scoop/porté) "module" fait que la fonction définie s'execute UNE SEULE fois pour tout les tests
def setup_module(module):
    print("ouvrire la base de donnée")

def teardown_module(module):
    print("Fermer la base de donnée")

def setup_function(function):
    print("ouvrire le navigateur")

def teardown_function(function):
    print("Fermer le navigateur")



def test_login():
   #print("ouvrire le navigateur")
    print("Ce connecter sur google")
    #print("Fermer le navigateur")
def test_creerCompte():
    #print("ouvrire le navigateur")
    print("Creer un compte google")
    #print("Fermer le navigateur")


def test_reenitialiserPass():
    #print("ouvrire le navigateur")
    print("Reenitialiser mot de pass")
    #print("Fermer le navigateur")