n = int(input('hoeveel getallen? '))

#moet je zetten want 1 past niet in de lus
vorige, huidige = 1, 1

for i in range(2, n):
    vorige, huidige = huidige, vorige + huidige

print(huidige)