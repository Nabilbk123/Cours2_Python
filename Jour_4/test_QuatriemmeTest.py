"""
Utilisation d'un autre concept basé sur des annotations a la place de "setup & teardown"



"""


import pytest

### le module: est la suite de tests / le fichier python dans le quel nous avons ecris nos tests
### Le parametre (scoop/porté) "module" fait que la fonction définie s'execute UNE SEULE fois pour tout les tests
# def setup_module(module):
#     print("ouvrire la base de donnée")
#
# def teardown_module(module):
#     print("Fermer la base de donnée")
#
# def setup_function(function):
#     print("ouvrire le navigateur")
#
# def teardown_function(function):
#     print("Fermer le navigateur")


### Creation de 2 fonctions qui joue le meme role que les fonctions du DeuxiemmeTest (presconditions & postconditions)
### En utilisant des annotations (pytest) et executer le "scope"
### En Rappelant que pour le "scope "module"" => Cela appliquera notre "instruction" UNE SEULE FOIS pour l'enssemble des tests (i.e: Tout le fichier
### Concernant le "scope: "function"" => Cela appliquera notre "instruction" Pour CHAQUE fonction (test) individuellement.


@pytest.fixture(scope="module")
def setup():
    print("ouvrire la base de donnée")
    yield
    print("Fermer la base de donnée")

### Le parametre "yield" => Donne instruction de Temporiser jusqu'a la fin du "module" ou "fonction" pour executer la seconde Instruction

@pytest.fixture(scope="function")
def before():
    print("ouvrire le navigateur")
    yield
    print("Fermer le navigateur")

@pytest.mark.usefixtures("setup","before")
def test_login():
   #print("ouvrire le navigateur")
    print("Ce connecter sur google")
    #print("Fermer le navigateur")


@pytest.mark.usefixtures("setup", "before")
def test_creerCompte():
    #print("ouvrire le navigateur")
    print("Creer un compte google")
    #print("Fermer le navigateur")

@pytest.mark.usefixtures("setup","before")
def test_reenitialiserPass():
    #print("ouvrire le navigateur")
    print("Reenitialiser mot de pass")
    #print("Fermer le navigateur")