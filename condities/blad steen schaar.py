s1 = input('speler 1: ')
s2 = input('speler 2: ')

if s1 == s2:
    print('onbeslist')
elif (s1 == 'blad' and s2 == 'schaar') or (s1 == 'steen' and s2 == 'blad') or (s1 == 'schaar' and s2 == 'steen'):
    print('speler 2 wint')
else:
    print('speler 1 wint')