# invoer
x = input('geef het eerste getal: ')
y = input('geef het tweede getal: ')

# twee absolute waardes
abs1 = abs(abs(float(x)) - abs(float(y)))
abs2 = abs(float(x) - float(y))

# afronden
a = round(abs1, 4)
b = round(abs2, 4)

# uitvoer
print(str(a) + ' \N{LESS-THAN OR EQUAL TO} ' +str(b))