getal = int(input('geef getal: '))

som = 0

for veelvoud in range(getal, 101, getal):
    som += veelvoud

print(som)