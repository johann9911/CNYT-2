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

def sumaCV(V):
    suma = (0, 0)
    for vc in V:
        suma = sumaC(suma[0], suma[1], vc[0], vc[1])
    return suma

def isValidMM(M,M1):
    valid = True
    if len(M) != len(M1):
        valid = False
    else:
        for fil in range(len(M)):
            if len(M[fil]) != len(M1[fil]):
                valid = False
    return valid

def isValidMV(M,V):
    valid = True
    for fil in range(len(M)):
        if len(M[fil]) != len(V):
            valid = False
    return valid

def productoMM(M,M2):
    res = []
    if isValidMM(M,M2) == False:
        raise ValueError('El número de columnas de M debe ser igual al número de filas de M2')
    else:
        M2 = traspuestaM(M2)
        for fil in range(len(M)):
            subres = []
            for fil2 in range(len(M2)):
                V = productoVV(M[fil2],M2[fil])
                subres.append(sumaCV(V))
            res.append(subres)
        res = traspuestaM(res)
    return res

def productoVV(V,V2):

    if len(V) != len(V2):
        raise ValueError('V y V2 deben tener la misma dimension')
    else:
        res=[]
        for fil in range(len(V2)):
            res.append(productoC(V[fil][0],V[fil][1],V2[fil][0],V2[fil][1]))

        return res

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
        return x, y

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
    return r, θ

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
        raise ValueError('u y v deben tener el mismo tamano')
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

def productoCV(r,V):
    res = []  # Contenedor de la respuesta
    for v in range(len(V)):
        res.append(productoC(r[0],r[1],V[v][0],V[v][1]))
    return res

def normaV(V):
    suma = 0
    for v in range(len(V)):
        suma+= (V[v][0])**2 #Real
        suma+= (V[v][1])**2 #Imaginario

    res = math.sqrt(suma)
    return res

def distanciaV(V,V2):
    a, b = 0, 0  #inicialzamos suma de partes de los complejos

    if len(V)!= len(V2):
        raise ValueError('V y V2 deben tener el mismo tamano')
    else:
        for fil in range(len(V)):
            a+= (V[fil][0] - V2[fil][0])**2
            b+=  (V[fil][1] - V2[fil][1])**2
        res = math.sqrt(a+b)
    return res

def productoInternoVV(V,V2):
    if len(V) != len(V2):
        raise ValueError('V y V2 deben tener la misma dimension')
    else:
        a, b = 0, 0
        for fil in range(len(V2)):
            cV = conjugadoC(V[fil][0],V[fil][1])
            res = productoC(cV[0],cV[1],V2[fil][0],V2[fil][1])
            a+= res[0]
            b+= res[1]
        return (a, b)

#Matrices

def sumaM(M,M1): #Matrices deben tener el mismo tamano
    res = [] # Contenedor de la respuesta
    if isValidMM(M,M1) == False:
        raise ValueError('M y M1 deben tener la misma dimension')
    else:
        for fil in range(len(M)):
            subres = [] #Sub contenedor
            for col in range (len(M[0])):
                subres.append(sumaC(M[fil][col][0], M[fil][col][1], M1[fil][col][0], M1[fil][col][1]))
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

def productoCM(c, M):
    res = []  # Contenedor de la respuesta
    for fil in range(len(M)):
        subres = []  # Sub contenedor
        for col in range(len(M[0])):
            subres.append(productoC(c[0], c[1], M[fil][col][0], M[fil][col][1]))
        res.append(subres)
    return res

def traspuestaM(M):
    res = []  # Contenedor de la respuesta
    for fil in range(len(M[0])):
        subres = []
        for col in range(len(M)):
            subres.append(M[col][fil])
        res.append(subres)
    return  res

def conjugadaM(M):
    res = []  # Contenedor de la respuesta
    for fil in range(len(M)):
        subres = []
        for col in range(len(M[0])):
            subres.append(conjugadoC(M[fil][col][0], M[fil][col][1]))
        res.append(subres)
    return  res

def adjuntaM(M):
    return traspuestaM(conjugadaM(M))

def accionMV(M,V):
    if isValidMV(M,V) == False:
        raise ValueError('Las columnas de M y V deben tener la misma dimension')
    else:
        res = []
        for fil in range(len(M)):
            for col in range(len(M[0])):
                MV = productoVV(M[fil],V)
                suma = sumaCV(MV)
            res.append(suma)
    return res

def isUnitaria(M):
    valido = True
    res = productoMM(M,adjuntaM(M))
    for fil in range(len(res)):
        for col in range(len(res[0])):
            if fil == col and valido == True:
                if res[fil][fil] != (1,0):
                    valido = False
            else:
                if valido == True:
                    if res[fil][col] != (0, 0):
                        valido = False
    return valido

def isHermitiana(M):
    valido = True
    res = adjuntaM(M)
    for fil in range(len(M)):
        for col in range(len(M[0])):
            if res[fil][col] != M[fil][col] and valido == True:
                    valido = False
    return valido