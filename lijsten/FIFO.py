invoer = input('geef string: ')

# queue
lijst = []

# wanneer vraagteken EN het mag geen lege lijst zijn
while invoer != 'STOP':
    if invoer == '?' and len(lijst) != 0:
        print(lijst.pop(0))

# niet gelijk aan vraagteken
    elif invoer != '?':
        lijst.append(invoer)

    invoer = input('geef string: ')