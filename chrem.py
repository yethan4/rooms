def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)

    if b == 0:
        return (a, 1, 0)

    sPrev = 1
    tPrev = 0
    sCur = 0
    tCur = 1

    while True:
        q = a // b  
        r = a % b   
        a = b
        b = r

        if b == 0:
            return (a, sCur, tCur)

        sNew = sPrev - q * sCur  
        tNew = tPrev - q * tCur  

        sPrev = sCur
        tPrev = tCur
        sCur = sNew
        tCur = tNew

def chrem(congruence1, congruence2):
    (a1, n1) = congruence1
    (a2, n2) = congruence2

    (d, s, t) = extended_gcd(n1, n2)

    if d == 1:
        solution = n1 * a2 * s + n2 * a1 * t
        modulo = n1 * n2
        return (solution % modulo, modulo)

    if (a1 - a2) % d != 0:
        return None

    lcm_modulo = (n1 // d) * n2
    k = (a1 - a2) // d
    solution = a1 - n1 * s * k

    return (solution % lcm_modulo, lcm_modulo)


def chrem_multiple(congruences):
    if len(congruences) == 0:
        return None
    if len(congruences) == 1:
        return congruences[0]
    
    solution = chrem(congruences[0], congruences[1])

    if solution == None:
        return None


    for congruence in congruences[2:]:
        solution = chrem(solution, congruence)

        if solution == None:
            return None

    return solution

