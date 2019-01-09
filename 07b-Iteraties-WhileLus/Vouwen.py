dikte = int(input('geef de dikte van het papier: '))
afstand = int(input('geef de afstand tot het hemellichaam: '))

vouwen = 0
nieuwe_dikte = 0

while dikte < afstand:
    dikte = dikte * 2
    nieuwe_dikte = dikte
    vouwen += 1

print('Na {} keer vouwen bedraagt de dikte van het papier {} mm.'.format(vouwen, nieuwe_dikte))