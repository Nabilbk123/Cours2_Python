### Differentes facons de representer "une chaine de caractéres"
#### Ce Type est TRES IMPORTANT pour notre cours ###

s1="Automatisation de tests"
s2='Tests manuel'
s3=""" Test automatisés 
avec Selenium
"""                           #### Avec la facon pour "s3" et "s4" on  poura GARDER la FORME (saut a la ligne)
s4='''Tests automatisés 
avec RobotFramework
'''

#print(type(s1))
#print(type(s2))
#print(type(s3))
#print(type(s4))



### Verifier les differents facons :
### Les differences : Avec s3 et s4 >> On peut GARDER la MISE EN FORME original
#print(s1)
#print(s2)
print(s3)
print(s4)


#s5="L'hiver prochaine il va faire chaud"
#s6='''Cet hiver est 'excessivement' froid'''  #### Pour que Python comprenne et garde les '..' dans toute la chaine de caracteres
#print(s6)

#############
###Le slicing de chaine de caractéres (découpage de la chaine de caractére)###

##Pour afficher la taille d'une chaine de caracétere:
s1="Automatisation de tests"
print(len(s1))
##Pour recuperer le 'A' : Sachant que l'indexation dans Python est '0' / Pour recuperer par exemple le 1ere 's'
print(s1[22])
### Deux facons de recuperer le caractere voulue :
### 1- Premiere facon: Comme l'exemple au dessus en commancant par chercher
### en commencer le comptage par le DEBUT (De Gauche a Droite) (premier index = 0) ###
### 2 - Deuxiemme facon: En commencant par la FIN (de Droite a Gauche) en metant le 'signe moins (-)'

### Par exemple: Chercher le dernier 's':
print(s1[-1])
### Par exemple: Chercher le dernier 't':
print(s1[-2])

##### Pour grouper:
s1="Automatisation de tests"
s2='Tests manuel'
s8=s1+""+s2
print(s8)
### Le resultat du print: Automatisation de testsTests manuel

### Pour multiplier le text fois 9 par exemple:
s9=s1*9
print(s9)

