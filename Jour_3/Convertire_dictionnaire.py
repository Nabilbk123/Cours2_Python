## Transformation "Dictionnaire python en texe "json"
##Variable "python" sous forme de dictionnaire
import json

etudiant={"nom":"Nabil","id":123,"specialité":"assurance Qualité"}
print(type(etudiant))

##Stocker notre variable dictionnaire python en forme json (sous forme de caractere):

## Utiliser la methode: "dumps"
etudiant_json=json.dumps(etudiant)
print(type(etudiant_json))



