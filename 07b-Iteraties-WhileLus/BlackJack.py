waarde = int(input('geef de waarde van de kaart: '))
score = waarde

while (score < 21) and (waarde != 0):
    waarde = int(input('geef de waarde van de kaart: '))
    score += waarde

if score == 21:
    antwoord = 'Gewonnen!.'
elif score > 21:
    antwoord = 'Verbrand ({})'.format(score)
else:
    antwoord = 'Voorzichtig gespeeld ({})'.format(score)

print(antwoord)

