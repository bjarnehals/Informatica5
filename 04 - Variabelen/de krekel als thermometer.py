N60 = int(input('geef het aantal tjirps per minuut: '))

Tf = 50 + ((N60 - 40) / 4)
Tc = 10 + ((N60 - 40) / 7)

print('temperatuur (Fahrenheit): ' + str(Tf))
print('temperatuur (Celsius): ' + str(Tc))


