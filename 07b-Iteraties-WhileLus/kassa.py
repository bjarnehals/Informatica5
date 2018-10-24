prijs = float(input('geef de prijs: '))
totaal = prijs

while prijs > 0:
    prijs = float(input('geef de prijs: '))
    totaal += prijs

print('De totale prijs is € {:.2f}'.format(totaal))