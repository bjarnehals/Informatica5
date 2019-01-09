tijdstip = int(input('geef het tijdsstip: '))

totaal = 0

for stappen in range(0, tijdstip + 1):
    if stappen % 2 == 0:
        totaal -= stappen / 2
    else:
        totaal += stappen + 1

print(int(totaal))