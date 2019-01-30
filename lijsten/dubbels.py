def dubbels(lijst):

    # lijst dubbels
    lijst_dubbels = []

    # gevonden dubbel --> als huidig element meer dan 1 keer voorkomt
    for element in lijst:
        if lijst.count(element) > 1 and not element in lijst_dubbels:
            lijst_dubbels.append(element)

    #zndere lijst teruggeven
    return lijst_dubbels