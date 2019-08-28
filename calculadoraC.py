import math

gradosPC = math.pi / 180 #Conversion de grados a radianes
gradosCP = 180 / math.pi  # Conversion de radianes a grados

#Funciones adicionales
def inversa(a,b):
    # inversa del # real
    b, a = conjugadoC(b, a)
    # inversa de # imaginario
    a, b = conjugadoC(a, b)
    return (a, b)


#Funciones principales
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
        raise ValueError('A y B deben tener el mismo tamano')
    else:
        for fil in range(len(u)):
           res.append(sumaC(u[fil][0],u[fil][1], v[fil][0], v[fil][1]))
    return res

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

def sumaM(A,B): #Matrices deben tener el mismo tamano
    res = [] # Contenedor de la respuesta
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError('A y B deben tener la misma dimension')
    else:
        for fil in range(len(A)):
            subres = [] #Sub contenedor
            for col in range (len(A[0])):
                subres.append(sumaC(A[fil][col][0], A[fil][col][1], B[fil][col][0], B[fil][col][1]))
            res.append(subres)
    return res

def inversaM(M):
    res = []  # Contenedor de la respuesta
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

def traspuestaM(M):
    res = []  # Contenedor de la respuesta
    for i in range(len(M[0])):
        subres = []
        for j in range(len(M)):
            subres.append(M[j][i])
        res.append(subres)
    return  res

def conjugadaM(M):
    res = []  # Contenedor de la respuesta
    for i in range(len(M[0])):
        subres = []
        for j in range(len(M)):
            subres.append(conjugadoC(M[i][j][0], M[i][j][1]))
        res.append(subres)
    return  res

def adjuntaM(M):

    return traspuestaM(conjugadaM(M))


'''def productoM2(M, M2):
    res = [] # Contenedor de la respuesta
    for fil in range(len(M)):
        for j in range (len(M2)):
            (M[i][j] * M2[i][j]) + (M[i][j+1] * M2[i+1][j]) 
    return res'''

#print(traspuestaM([[1,2],[3,4]]))
#print(conjugadaM([[(1,2),(-3,5)],[(3,4),(-1,-1)]]))
#print(traspuestaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]))
#print(conjugadaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]))
#print(adjuntaM([[(6,-3),(2,12),(0,-19)], [(0,0),(5,2.1),(17,0)], [(1,0),(2,5),(3,-4.5)]]))
#print(inversaM([[(-3,1),(4,1)], [(-2,1),(2,1)],[(0,-1),(3,1)]]))
