a = int(input('het uur van vertrek thuis: '))
b = int(input('het aantal minuten van vertrek thuis: '))
c = int(input('het uur van aankomst vriendin: '))
d = int(input('het aantal minuten van aankomst vriendin: '))
e = int(input('het uur van vertrek vriendin: '))
f = int(input('het aantal minuten van vertrek vriendin: '))
g = int(input('het uur van aankomst thuis: '))
h = int(input('het aantal minuten van aankomst thuis: '))

U = ((g - a) - (e - c)) / 2
min = ((h - b) - (f - d)) / 2

#geen negatieve waarden toegelaten en rekening houden met max 24u en max 60min
uur = e + U
minuten = f + min

print(int(uur))
print(int(minuten))