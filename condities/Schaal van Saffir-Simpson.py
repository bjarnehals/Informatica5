windsnelheid = int(input('geef de windsnelheid: '))

if windsnelheid >= 250:
    cat = 'categorie 5'
elif windsnelheid >= 210:
    cat = 'categorie 4'
elif windsnelheid >= 178:
    cat = 'categorie 3'
elif windsnelheid >= 154:
    cat = 'categorie 2'
elif windsnelheid >= 119:
    cat = 'categorie 1'
else:
    cat = 'geen orkaan'

print(cat)