#vraag coëficiënten bij x^1 en x^0 van een tweedegraadsfunctie f(x) = ax^2 + bx^2 + bx^1 + cx^0
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

#bereken de discriminant
discriminant = b ** 2 - (4 * a * c)

#uitvoer
print('discriminant =', discriminant)
