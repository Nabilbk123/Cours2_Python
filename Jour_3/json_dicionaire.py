###On va importer (mettre a disposition)un package(ensemble de classe et de methodes qui traitent une fonctionnalité particuliére / librairie) pour manipuler des fichiers
###"json"

import json
### Fichier "json" sous forme de chaine de caractére
data='''{
    "nom": "Nabil",
    "salaire": 120000,
    "langages": [
        "Java",
        "pyhon",
        "javascript"
    ],
    "adresse": {
        "numero appart": 19,
        "ville": "Montreal",
        "telephone": {
            "mobile": 514514514,
            "fixe": 514723723
        }
    }
}'''
print(type(data))
data_dic = json.loads(data)
print(type(data_dic))
### La methode "loads" va transformer notre fichier "json" qui est sous forme de caractere et va le CONVERTIR en Dictionaire:
### Par ce fait je pourais MANIPULER le fihcier json comme un type de Python maintenant :)
### Notre "json" est maintenant stocké en forme de dictionnaire
#print(data_dic)
#print(data_dic["salaire"])
#print(data_dic["adresse"],[telephone])
print(data_dic["adresse"]["telephone"]["fixe"])
### On utilise (array notation pour trouver le path)
### Presque de la meme maniere que dans les fichiers jason