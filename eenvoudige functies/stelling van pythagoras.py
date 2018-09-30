a = float(input('geef a: '))
b = float(input('geef b: '))

from math import sqrt

c = sqrt(pow(a, 2) + pow(b, 2))

a_afgerond = '{:.2f}'.format(a)
b_afgerond = '{:.2f}'.format(b)
c_afgerond = '{:.2f}'.format(c)

print('In een rechthoekige driekhoek met rechthoekzijden a = ' + str(a_afgerond) + ' en b = ' + str(b_afgerond) + ' is de schuine zijde ' + str(c_afgerond))