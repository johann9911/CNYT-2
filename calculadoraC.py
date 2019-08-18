import math

gradosPC = math.pi / 180 #Conversión de grados a radianes
gradosCP = 180 / math.pi  # Conversión de radianes a grados

def sumaC(a,b,c,d):
    z1 = a + c
    z2 = b + d
    return z1, z2

def restaC(a,b,c,d):
    z1 = a - c
    z2 = b - d
    return z1, z2

def productoC(a,b,c,d):
    z1 = (a*c - b*d)
    z2 = (a*d + b*c)
    return z1, z2

def divisionC(a,b,c,d):

    if c == 0 and d == 0:
        raise ValueError('Can not divide by zero!')
    else:
        z1 = (a * c + b * d)
        z2 = (c * b - a * d)
        z3 = (c ** 2 + d ** 2)
        return z1/z3, z2/z3


def polarCartesianoC(r, θ):
    if r == 0:
        return 0
    else:
        if θ == 0:
            x = r * math.cos(θ * gradosPC)
            y = 0
        else:
            x = r * math.cos(θ * gradosPC)
            y = r * math.sin(θ * gradosPC)

        return round(x,2),round(y,2)

def cartesianoPolarC(x, y):

    r = math.sqrt((x ** 2 + y ** 2))

    if x == 0 and y == 0:
        θ = 0
    elif x == 0 and y > 0:
        θ = 90
    elif x ==0 and y < 0:
        θ = -90
    else:
        arcT = math.atan((y / x)) * gradosCP

    # Determinar k
        if x > 0:
            k = 0
        else:
            k = 1

        θ = arcT + 180 * k
    return round(r, 2),round(θ, 1)

def moduloC(a, b):
    z = math.sqrt(a**2 + b**2)
    return round(z, 2)

def conjugadoC(a,b):
    if b < 0: b = abs(b)
    else: b = -b
    return a, b

def faseC(x, y):

    if x == 0 and y ==0:
        θ = 0
    elif x == 0 and y > 0:
        θ = 90
    elif x ==0 and y < 0:
        θ = -90
    else:
        arcT = math.atan((y / x)) * gradosCP

        # Det k
        if x > 0:
            k = 0
        else:
            k = 1

        θ = arcT + 180 * k
    return θ
