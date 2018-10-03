a = int(input('geef a: '))
b = int(input('geef b: '))

c = a + b

print('{:>6d} + {:<6d} = {:<d}'.format(a,b,c))
print('{:>6d} + {:<6d} = {:<d}'.format(a * 10,b * 10,c * 10))
print('{:>6d} + {:<6d} = {:<d}'.format(a * 100,b * 100,c * 100))
print('{:>6d} + {:<6d} = {:<d}'.format(a * 1000,b * 1000,c * 1000))
print('{:>6d} + {:<6d} = {:<d}'.format(a * 10000,b * 10000,c * 10000))