def volgend_getal_collatz(getal):

    if getal % 2 == 0:
        getal /= 2
    else:
        getal = (getal * 3) + 1
    return getal

print(volgend_getal_collatz(27))



