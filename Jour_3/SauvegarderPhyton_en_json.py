import json

etudiant={"nom":"Nabil","id":123,"specialité":"assurance Qualité"}
print(type(etudiant))
## On ouvre le fichier ou l'on veut ecrire / on met "w" pour write
json_file=open("C:\\Users\\nabil\\PycharmProjects\\ScriptPhyton\\data.txt","w")
## On va utiliser la methode : json.dump pour ecrire (transformer et transferer) et Stocker
## Stocker : "etudiant"   dans  "json_file"
json.dump(etudiant,json_file)
with open()