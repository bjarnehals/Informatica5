def germaniseer(zin):
    nieuwe_zin = ' '
    for i in range(len(zin)):
        if zin[i - 1] == ' ':
            nieuwe_zin += zin[i].upper()
        else:
            nieuwe_zin += zin[i]
    return nieuwe_zin

print(germaniseer('Hallo ik ben bjarne'))