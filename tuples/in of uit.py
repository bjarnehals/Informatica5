from math import sqrt

def binnen_of_buiten(M, P, Q):

    plaats = ''

    d1 = sqrt(pow(P[0] - M[0], 2) + pow(P[1] - M[1], 2))
    d2 = sqrt(pow(Q[0] - M[0], 2) + pow(Q[1] - M[1], 2))

    if d1 < d2:
        plaats = 'buiten'

    elif d1 > d2:
        plaats = 'binnen'

    else:
        plaats = 'op'

    return plaats, round(d2, 4)


print(binnen_of_buiten((0, 0),(1, 1),(-1, -1)))