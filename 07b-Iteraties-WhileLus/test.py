bod = float(input('startprijs: '))
doorgedraaid = float(input('doorgedraaid onder: '))
akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

# zolang (er geen bod is) en (zolang er nog iets van de prijs kan gedaan worden)
while (not akkoord) and (bod >= doorgedraaid + 0.01):
 bod -= 0.01

 # is er nu iemand geïnteresseerd?
 akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

if akkoord:
 print('verkocht aan {:.2f}'.format(bod))
else:
 print('doorgedraaid')