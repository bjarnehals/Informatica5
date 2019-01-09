def splits(getal):
    c1 = int(str(getal)[0])
    c2 = int(str(getal)[1])
    c3 = int(str(getal)[2])
    c4 = int(str(getal)[3])

    return c1, c2, c3, c4

def oplopende_cijfers(c1, c2, c3, c4):
    # van klein naar groot: s1, s2, s3, s4
    s1 = min(c1, c2, c3, c4)
    s4 = max(c1, c2, c3, c4)
    # het middelgrote getal van c1, c2, c3 is een kandidaat voor s2 en s3
    k1 = max(min(c1, c2), min(c1, c3), min(c2, c3))
    k2 = c1 + c2 + c3 + c4 - s1 - s4 - k1

    # s2 en s3
    s2 = min(k1, k2)
    s3 = max(k1, k2)

    return s1, s2, s3, s4

def op_af_getallen(s1, s2, s3, s4):
    op = str(s1) + str(s2) + str(s3) + str(s4)
    af = op[::-1]
    return op, af

def verschil(aflopend, oplopend):
    uitkomst = int(aflopend) - int(oplopend)
    return str(uitkomst)

def kaprekar(getal):

    bewerkingen = ''

    while getal != 6174:
        a, b, c, d = splits(getal)
        w, x, y, z = oplopende_cijfers(a, b, c, d)
        op, af = op_af_getallen(w, x, y, z)
        getal = int(verschil(af, op))
        bewerkingen += af + ' - ' + op + ' = ' + str(getal) + '\n'

    return bewerkingen[:-1]

