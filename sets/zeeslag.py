def boot_overlappend(boot_1, rooster):
    if boot_1.isdisjoint(rooster) == True:
        antwoord = False
    else:
        antwoord = True

    return antwoord


def boot_toevoegen(boot_1, rooster):
    if boot_overlappend(boot_1, rooster) == True:
        antwoord = rooster
    else:
        antwoord = boot_1.union(rooster)

    return antwoord

def vuur(co, rooster):
    if co in rooster:
        rooster.discard(co)
        antwoord = True
    else:
        antwoord = False

    return antwoord, rooster