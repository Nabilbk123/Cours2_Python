a=10
print(type(a))

#Systéme numérique: décimal
#On peut representer le systeme numérique en plusieurs formes : décimal, binaire, hexadecimal et octal

###Representation binaire: (representation d'un nombre en base2 >> de 0 a 1)
#somme=0b01111
#total=0B00111
#print(total)

###Representation en base "octal": (representation en base 7 >> de 0 a 7)
###Il faut commencer ce nombre par la lettre "o" ou "O"(majuscule)
#b=0o3175206
#print(b)
#c=0O054732
#print(c)

###Representation en base "hexadicimal":  (de 0 a 9 et de a a f)
#d=0xface
#print(d)


###Convertions de base###

####### Commentaire 1 : Converstion binaire (en utilisant le méthode Python "bin"
######                  Pour representer n'importe quel "entier" en nombre "binaire"
k=25
print(bin(k))

####### Commentaire 2 : Converstion octale >> Utilisant le méthode "oct"
print(oct(k))

####### Commentaire 3 : Converstion hexadécimal >> Utilisant le methode "hex"
print(hex(k))