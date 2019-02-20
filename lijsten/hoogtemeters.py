def hoogtemeters(hoogtes):
    # hoogtes overlopen en het verchil pakken tussen 2 opeenvolgende hoogtes

    lijst_nieuwe_hoogtes = []
    for i in range(1, len(hoogtes)):
       lijst_nieuwe_hoogtes.append(hoogtes[i] - hoogtes[i - 1])
    return lijst_nieuwe_hoogtes

def dalen_en_stijgen(hoogtes):

    daling_en_stijging = [0, 0]

    for i in hoogtes:
        if i < 0:
            daling_en_stijging[0] += abs(i)
        else:
            daling_en_stijging[1] += i

    return tuple(daling_en_stijging)

print(dalen_en_stijgen([-761, 286, -113, 649, -547]))
