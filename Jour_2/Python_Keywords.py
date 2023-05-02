###Retrouver les mots reservés de Phyton (Keywords)###

#Il faut pour cela d'abord "importer un package" (Package=Ensemble de méthode et de classes natives dans Phyton)

import keyword
#Pour lister et printer la "kwlist"
#print(keyword.kwlist)

#Pour compter le nombre de ce qu'il y'a a l'interieur > Utiliser la méthode : "len"
print(len(keyword.kwlist))
# Introduction de la notion d'"IDENTIFIANTS" qui lui ENGLOVE les "Variable et les Fonctions ou Classes"
#IDENTIFIANT sont : tous ce que l'on crée dans Phyton (a savoir : les Variables, les Classes, les Fonctions, Objets,..)
a=25

#Les identifiant doivent etre IMPERATIVEMENT different des "keywords" de Phyton
# exemple: as=25

#123somme=25  >> Les "identifiant ne doivent pas COMMANCER par un nombre
some123=25  #Ca c'est okay comme cela par exemple
#somme$=25    >> Les "identifiant ne doivent pas CONTENIR de caractéres spéciaux
