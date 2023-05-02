

# nbr1=input('svp entrez un nombre : ')
# nbr2=input('svp entrez un second nombre : ')

### Il va nous dire de quelle type : 'int' ou 'string'###
# print(type(nbr1))
# print(type(nbr2))

### Il faut d'abord CONVERTIR toute que cette fonction nous retourne en : ENTIER (int)###
### Utiliser donc 'int()' ###

nbr1=int(input('svp entrez un nombre : '))
nbr2=int(input('svp entrez un second nombre : '))

print(type(nbr1))
print(type(nbr2))

if(nbr1>nbr2):
    print('Le premier nombre est plus grand que le second' +str(nbr1))  ### On utilise la methode 'str'
elif(nbr1==nbr2):                                                       ### Pour convertir le 'int' on String
    print('les deux nombres sont égaux')
else: print('le second nombre est le plus grand' +str(nbr2))

