def is_letter(letter):
    antwoord = False
    letter = ord(letter)

    if letter >= ord('A') or letter <= ord('z'):
        antwoord = True

    return antwoord

def roteer_letter(letter, getal):
    if is_letter(letter) == True:
        nieuwe_letter = ord(letter) + getal
        if 

roteer_letter('g', 1)
print(nieuwe_letter)

