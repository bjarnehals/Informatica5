def hint(gok, oplossing):
    ht = ''

    #overloop alle letters van gok
    for i in range(0, len(gok)):

        # controleer of letter van gok voorkomt in oplossing
        if oplossing.find(gok[i]) != -1:
            if gok[i] == oplossing[i]:
            # ja --> juiste plaats: hoofdletter
                ht += gok[i].upper()
            else:
                #ja --> niet juiste plaats: kleine letter
                ht += gok[i].lower()
        else:
            #nee --> .
            ht += '.'

        return ht


print(hint('zoets', 'zager'))