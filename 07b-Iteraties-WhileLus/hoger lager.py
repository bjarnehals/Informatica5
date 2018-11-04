from random import randint
getal = randint(1, 100)

begin = 1
eind = 100
pogingen = 0

gok = randint(1, 100)

while gok != getal:
    gok = randint(begin, eind)
    print('[{}, {}] --> computer gokt {}'.format(begin, eind, gok))
    if gok < getal:
        begin = gok + 1
    elif gok > getal:
        eind = gok - 1
    pogingen += 1

print('computer had {} pogingen nodig om het getal {} te raden.'.format(pogingen, getal))


