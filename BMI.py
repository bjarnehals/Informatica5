l = float(input('geef de gelijke lengte van de twee personen: '))
naam_1 = str(input('geef de naam van de eerste persoon: '))
gew_1 = float(input('geef het gewicht van de eerste persoon: '))
naam_2 = str(input('geef de naam van de tweede persoon: '))
gew_2 = float(input('geef het gewicht van de tweede persoon: '))

bmi_1 = gew_1 / pow(l, 2)
bmi_2 = gew_2 / pow(l, 2)

if bmi_1 > bmi_2:
    hoogst_bmi = float(bmi_1)
else:
    hoogst_bmi = float(bmi_2)

if bmi_1 > bmi_2:
    hoogst_naam = naam_1
else:
    hoogst_naam = naam_2

if hoogst_bmi >= 30:
    antwoord = 'is obees.'
elif hoogst_bmi >= 25:
    antwoord = 'heeft overgewicht.'
elif hoogst_bmi >= 18.5:
    antwoord = 'heeft een gezond gewicht.'
else:
    antwoord = 'heeft ondergewicht.'

bmi_afg = '{:.2f}'.format(hoogst_bmi)

print(hoogst_naam + ' heeft het hoogste BMI (' + str(bmi_afg) + ') en ' + antwoord)
