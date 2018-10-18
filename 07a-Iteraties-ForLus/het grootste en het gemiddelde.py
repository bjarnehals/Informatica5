aantal_getallen = int(input('hoeveel getallen? '))

som = 0
grootst = -1000

for i in range(0, aantal_getallen):
    getal = int(input('geef een getal: '))
    som += getal
    if getal > grootst:
        grootst = getal
    gemiddelde = som/aantal_getallen

print('Het grootste getal is {} en het gemiddelde is {:.2f}'.format(grootst, gemiddelde))


