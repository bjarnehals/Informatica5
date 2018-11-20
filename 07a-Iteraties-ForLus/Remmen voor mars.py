gewenst = int(input('geef de gewenste snelheid: '))
snelheid = int(input('geef de huidige snelheid: '))

rembewegingen = 0

while snelheid > gewenst:
    snelheid = snelheid - ((snelheid / 100) * 30)
    rembewegingen += 1

print('na {} rembewegingen is de snelheid {:.2f}'.format(rembewegingen, snelheid))

