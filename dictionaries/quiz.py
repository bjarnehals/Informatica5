def verlaat_ploeg(persoon, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].remove(persoon)
        if inschrijvingen[ploeg] == []:
            inschrijvingen.pop(ploeg)

    return inschrijvingen

def vervoegt_ploeg(persoon, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg] += [persoon]
    else:
        inschrijvingen[ploeg] = [persoon]

    return inschrijvingen






print(vervoegt_ploeg('Piet','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))



