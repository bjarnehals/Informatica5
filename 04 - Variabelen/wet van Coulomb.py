#invoer straal
r = float(input('geef de straal: '))

#gegevens
k = 8.99 * (10 ** 9)
q1 = 2.0 * (10 ** (-6))
q2 = 1.0 * (10 ** (-6))

#formule
Fc = k * ((q1 * q2) / (r ** 2))

#uitvoer
print(Fc * (10 ** 4))

