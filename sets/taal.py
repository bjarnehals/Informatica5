def behoort_tot_taal(woord, taal):
   if woord == ' ':
      antwoord = False
   else:
      letters = set(woord)
      letters.discard(' ')
      antwoord = letters.issubset(taal)

   return antwoord

def is_onleesbaar(woord, taal):
   letters = set(woord)

   return letters.isdisjoint(taal)

def perfect_woord(woord, taal):
   letters = set(woord)

   return letters.issuperset(taal)


