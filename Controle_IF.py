#
# ###Pour demander a l'utilisateur d'entrer: Utiliser "input"
#
# nom=input('entrez votre nom :  ')
#
# if (nom=='Mokhtar'):
#     print('Azule Mokhtar')
# else:print("Tu n'es pas la bonne personne")
#
#
#
#

#### Utilisation de "elif" : Ajouter une verification additionelle ####

equipe=input('quelle est ton equipe preferée?: ')
if(equipe=='JSK'):
    print('Est ce que Lyes est present : ')
elif(equipe=='Mouloudia'):
    print('Combien de but Mokhtar a marqué? : ')
elif(equipe=='CRB'):
    print('combien de cartons jaune ont étés émis? : ')
else:
    print("Cette equipe n'est pas repertoriée")

