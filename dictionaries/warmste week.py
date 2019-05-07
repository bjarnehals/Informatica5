def gift_inschrijven(klas, klassen):
    if klas[0] in klassen:
        klassen[klas[0]] += klas[1]
    else:
        klassen[klas[0]] = klas[1]

    return klassen

