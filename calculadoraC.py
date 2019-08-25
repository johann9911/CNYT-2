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
    return round(z1,2), round(z2,2)

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
        # Determinar k
        if x > 0:
            k = 0
        else:
            k = 1
        θ = arcT + 180 * k
    return θ

#Vectores

def sumaV(u,v):
    res = [] #Contenedor de la respuesta
    if len(u) != len(v):
        raise ValueError('A y B deben tener el mismo tamaño')
    else:
        for fil in range(len(u)):
           res.append(sumaC(u[fil][0],u[fil][1], v[fil][0], v[fil][1]))
    return res

def inversa(a,b):
    # inversa del # real
    b, a = conjugadoC(b, a)
    # inversa de # imaginario
    a, b = conjugadoC(a, b)
    return (a, b)


def inversaV(V):
    res = [] # Contenedor de la respuesta
    for v in range(len(V)):
        a = V[v][0] #Real
        b = V[v][1] #Imaginario
        res.append(inversa(a,b))
    return res

def productoV(r,V):
    res = []  # Contenedor de la respuesta
    for v in range(len(V)):
        res.append(productoC(r[0],r[1],V[v][0], V[v][1]))
    return res

#Matrices

def sumaM(A,B): #Matrices deben tener el mismo tamaño
    res = [] # Contenedor de la respuesta
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError('A y B deben tener la misma dimensión')
    else:
        for fil in range(len(A)):
            subres = [] #Sub contenedor
            for col in range (len(A[0])):
                subres.append(sumaC(A[fil][col][0], A[fil][col][1], B[fil][col][0], B[fil][col][1]))
            res.append(subres)
    return res

def inversaM(M):
    res = []  # Contenedor de la respuesta
    if len(M) != len(M[0]):
        raise ValueError('M debe ser una matriz cuadrada.')
    else:
        for fil in range(len(M)):
            subres = [] #Sub contenedor
            for col in range(len(M[0])):
                subres.append(inversa(M[fil][col][0], M[fil][col][1]))
            res.append(subres)
    return res

def productoM(c, M):
    res = []  # Contenedor de la respuesta
    for fil in range(len(M)):
        subres = []  # Sub contenedor
        for col in range(len(M[0])):
            subres.append(productoC(c[0], c[1], M[fil][col][0], M[fil][col][1]))
        res.append(subres)
    return res
