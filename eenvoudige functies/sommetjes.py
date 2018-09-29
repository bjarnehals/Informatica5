a = int(input('geef a: '))
b = int(input('geef b: '))

som1 = a + b
som2 = (a * 10) + (b * 10)
som3 = (a * 100) + (b * 100)
som4 = (a * 1000) + (b * 1000)
som5 = (a * 10000) + (b * 10000)

print('{:>6d}'.format(a) + ' + ' + '{:<6d}'.format(b) + ' = ' + '{:<6d}'.format(som1))
print('{:>6d}'.format(a * 10) + ' + ' + '{:<6d}'.format(b * 10) + ' = ' + '{:<6d}'.format(som2))
print('{:>6d}'.format(a * 100) + ' + ' + '{:<6d}'.format(b * 100) + ' = ' + '{:<6d}'.format(som3))
print('{:>6d}'.format(a * 1000) + ' + ' + '{:<6d}'.format(b * 1000) + ' = ' + '{:<6d}'.format(som4))
print('{:>6d}'.format(a * 10000) + ' + ' + '{:<6d}'.format(b * 10000) + ' = ' + '{:<6d}'.format(som5))