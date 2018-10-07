# invoer
worp_1 = int(input('geef de eerste worp van de aanvaller: '))
worp_2 = int(input('geef de tweede worp van de aanvaller: '))
worp_3 = int(input('geef de derde worp van de aanvaller: '))
worp_4 = int(input('geef de eerste worp van de verdediger: '))
worp_5 = int(input('geef de tweede worp van de verdediger: '))

# grootste worp van de aanvaller bepalen
if worp_1 >= worp_2 and worp_1 >= worp_3:
    grootst_a = worp_1
elif worp_2 >= worp_1 and worp_2 >= worp_3:
    grootst_a = worp_2
else:
    grootst_a = worp_3

# tweede grootste worp van de aanvaller bepalen
if (worp_1 >= worp_2 and worp_1 <= worp_3) or (worp_1 <= worp_2 and worp_1 >= worp_3):
    groot_a = worp_1
elif (worp_2 >= worp_1 and worp_2 <= worp_3) or (worp_2 <= worp_1 and worp_2 >= worp_3):
    groot_a = worp_2
else:
    groot_a = worp_3

# grootste worp van de verdediger bepalen
if worp_4 > worp_5:
    grootst_b = worp_4
    groot_b = worp_5
else:
    grootst_b = worp_5
    groot_b = worp_4

# uitkomst bepalen
if grootst_a > grootst_b and groot_a > groot_b:
    antwoord = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif (grootst_a < grootst_b and groot_a > groot_b) or (grootst_a > grootst_b and groot_a < groot_b)
    antwoord = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
elif (grootst_a == grootst_b and groot_a > groot_b) or (grootst_a > grootst_b and groot_a == groot_b):
    antwoord = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
elif (grootst_a == grootst_b and groot_a == groot_b) or (grootst_a < grootst_b and groot_a < groot_b)
    antwoord = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'
elif (grootst_a == grootst_b and groot_a < groot_b) or (grootst_a < grootst_b and groot_a == groot_b):
    antwoord = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'
else:
    antwoord = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'

# uitvoer
print(antwoord)
