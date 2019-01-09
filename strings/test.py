woord = input('Geef woord: ')

for i in range(len(woord)):
    if i % 2 == 0:
        print(woord[i + 1])