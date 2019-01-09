getal = int(input('geef een getal: '))

aantal = 0

for deler in range(1, getal):
    if getal % deler == aantal:
        som += deler

print(som)
