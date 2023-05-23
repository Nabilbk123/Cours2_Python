### Lire nos données a partir d'un fichier "data.json" en python
import json

#Utiliser la methode python - open / dans notre cas le fichier de donnée.json ce trouve dans notre racine ici
#ouvrire en mode "read==r"
fichier = open("C:\\Users\\nabil\\PycharmProjects\\ScriptPhyton\\data.json","r")
#Maintenant il est stocker comme une variable python dans "fichier"

data_json=json.load(fichier)
##on l'a transformer donc en dictionnaire phyton 
print(type(data_json))
print(data_json)