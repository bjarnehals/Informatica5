antwoord_1 = input('Trek aan de hendel van de wissel? ')
antwoord_2 = input('Man van de brug duwen? ')

doden = ''

if antwoord_1 == 'ja' and antwoord_2 == 'ja':
    doden = 2
elif (antwoord_1 == 'ja' and antwoord_2 == 'nee') or (antwoord_1 == 'nee' and antwoord_2 == 'ja'):
    doden = 1
elif antwoord_1 == 'nee' and antwoord_2 == 'nee':
    doden = 5

print(doden)
