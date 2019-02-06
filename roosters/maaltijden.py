def dagprijs(bestelling):

    prijs = 0

    for i in range(0, len(bestelling), 2):
        if bestelling[i] == 'middagmaal':
            prijs += 5.3 * bestelling[i + 1]
        elif bestelling[i] == 'soep':
            prijs += 1.7 * bestelling[i + 1]
        elif bestelling[i] == 'vieruurtje':
            prijs += 2.3 * bestelling[i + 1]

    return prijs

def weekprijs(bestelling):

    prijs = 0

    for dag in bestelling:
       prijs += dagprijs(dag)

    return prijs


