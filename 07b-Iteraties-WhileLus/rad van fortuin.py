woord = str(input('geef het woord: '))
bedrag = int(input('geef het geldbedrag: '))

letter = str(input('geef een letter: '))
totaal = 0
vorige_letter = ''

while (letter in woord) and (vorige_letter != letter):
    totaal += bedrag
    vorige_letter = letter
    letter = input(str('geef een letter: '))
print(totaal)
