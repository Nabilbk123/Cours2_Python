"""
Comment Regrouper les tests en utilisant la commande : pytest test_SixiemmeTest.py -s -v -m

Pour rappel : le "-s" pour afficher les caractéres , le "-v" pour afficher plus de contenu et :

"-m" pour => SELECTIONNE et Not Selectionner les tests voulus



"""


import pytest


@pytest.mark.regression
def test_Premier():
   #print("ouvrire le navigateur")
    print("PremierTest")
    #print("Fermer le navigateur")

@pytest.mark.regression
def test_Deuxiemme():
    #print("ouvrire le navigateur")
    print("DeuxiemmeTest")
    #print("Fermer le navigateur")

@pytest.mark.charge
def test_Troisiemme():
    #print("ouvrire le navigateur")
    print("TroisiemmeTest")
    #print("Fermer le navigateur")
@pytest.mark.charge
def test_Quatriemme():
    # print("ouvrire le navigateur")
    print("QuatriemmeTest")
    # print("Fermer le navigateur")

@pytest.mark.skip
def test_Cinquiemme():
    #print("ouvrire le navigateur")
    print("CinquiemmeTest")
    #print("Fermer le navigateur")

