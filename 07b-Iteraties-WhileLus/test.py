woord = input('woord: ')
bedrag = int(input('bedrag: '))

gewonnen_bedrag = 0
geraden_letter = ''

letter = input('letter: ')

while letter in woord and not letter in geraden_letter:
 gewonnen_bedrag += bedrag
 geraden_letter += letter
 letter = input('letter: ')

print(gewonnen_bedrag)

##########################################################

n = int(input('priemgetal: '))

# is modulo 0 bij het delen van n door alle getallen van 2 tot het getal zelf
# zolang de modulo verschillend van 0 is is het ok

i = 2
while(n // i != n/i) and i <= (n // 2) + 1:
  i += 1

if (i == n/2 + 1):
 print(str(n) + ' is een priemgetal')
else:
 print(str(n) + ' is geen priemgetal')