C = int(input('geef het aantal eurocent: '))

a = C // 100
b = C % 100
c = b // 50
d = b % 50
e = d // 20
f = d % 20
g = f // 10
h = f % 10
i = h // 5
j = h % 5
k = j // 2
l = j % 2
m = l // 1
n = l % 1

muntstukken = a + c + e + g + i + k + m

print(str(C) + ' cent kan je omwisselen in ' + str(muntstukken) + ' muntstukken')
print(str(a) + ' muntstukken van 1 euro')
print(str(c) + ' muntstukken van 50 cent')
print(str(e) + ' muntstukken van 20 cent')
print(str(g) + ' muntstukken van 10 cent')
print(str(i) + ' muntstukken van 5 cent')
print(str(k) + ' muntstukken van 2 cent')
print(str(m) + ' muntstukken van 1 cent')
print((str(float(C * (10 ** (-2))))) + ' euro in totaal')