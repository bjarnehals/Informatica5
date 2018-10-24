aantal = int(input('hoeveel getallen? '))

# eerste getal buiten de lus vragen, dan heb je direct al een grootste getal.
grootste = int(input('geef getal: '))
som = grootste

# aantal-1 want je eerste getal is al gegeven.
for i in range(aantal-1):
    getal = int(input('geef een getal: '))
    grootste  = max(grootste, getal)
    som += getal

print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootste, som / aantal))


