woord = str(input('geef het woord: '))
bedrag = int(input('geef het geldbedrag: '))

letter = ''
totaal = 0

while letter in woord:
    letter = input(str('geef een letter: '))
    if letter in woord:
        totaal += bedrag

print(totaal)
