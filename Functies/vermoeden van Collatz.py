def volgend_collatz_getal(getal):

    if getal % 2 == 0:
        getal /= 2
    else:
        getal = (getal * 3) + 1
    return int(getal)

def collatz(getal):

    cyclelengte = 0

    while getal >= 1:
        cyclelengte += 1
        if getal != 1:
            getal = volgend_collatz_getal(getal)
        else:
            return int(cyclelengte)






