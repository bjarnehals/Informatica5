keuze_1 = input('geef het eerste: ')
keuze_2 = input('geef het tweede: ')

if keuze_1 == 'blad' and keuze_2 == 'blad':
    winnaar = 'onbeslist'
elif keuze_1 == 'blad' and keuze_2 == 'steen':
    winnaar = 'speler 1 wint'
elif keuze_1 == 'blad' and keuze_2 == 'schaar':
    winnaar = 'speler 2 wint'
elif keuze_1 == 'steen' and keuze_2 == 'blad':
    winnaar = 'speler 2 wint'
elif keuze_1 == 'steen' and keuze_2 == 'schaar':
    winnaar = 'speler 1 wint'
elif keuze_1 == 'steen' and keuze_2 == 'steen':
    winnaar = 'onbeslist'
elif keuze_1 == 'schaar' and keuze_2 == 'schaar':
    winnaar = 'onbeslist'
elif keuze_1 == 'schaar' and keuze_2 == 'steen':
    winnaar = 'speler 2 wint'
elif keuze_1 == 'schaar' and keuze_2 == 'blad':
    winnaar = 'speler 1 wint'

print(winnaar)