#valentina Alvarado
#libreria de vectores y matrices que contienen numeros complejos
#valentina alvarado
#cnyt
#calculadora con numeros complejos

import math
from math import sqrt
def sumar(tpl1,tpl2):
    """ Esta función le ayuda a calcular la suma entre dos numeros complejos
        (tuple,tuple) ---> tuple"""
    sumareal = tpl1[0] + tpl2[0]
    sumaimg = tpl1[1] + tpl2[1]
    return (sumareal,sumaimg)
#
def multiplicar(tpl1,tpl2):
    """Esta función le ayuda a calcular la multiplicación entre dos numeros complejos
       (tuple,tuple)---> tuple"""
    answ = [tpl1[0] * tpl2[0] - tpl1[1] * tpl2[1],tpl1[1] * tpl2[0] + tpl1[0] * tpl2[1]]
    return answ
#
def resta(tpl1,tpl2):
    """ Esta funcion le ayuda a calcular la resta entre dos numeros complejos
        (tuple,tuple) ---> tuple"""
    restareal = tpl1[0] - tpl2[0]
    restaimg = tpl1[1] - tpl2[1]
    return (restareal,restaimg)
#
def dividir(tpl1,tpl2):
    """Esta funcion le ayuda a calcular la division entre dos numeros complejos
        (tuple,tuple)--->tuple"""
    denominador = (tpl2[0] * tpl2[0]) + (tpl2[1] * tpl2[1] )
    numer1 = (tpl1[0] * tpl2[0]) + (tpl1[1] * tpl2[1])
    numer2 = (tpl2[0] * tpl1[1]) - (tpl2[1] * tpl1[0])
    real1 = round(numer1 / denominador,3)
    imaginario = round(numer2 / denominador,3)
    return (real1,imaginario)
#
def modulo(tpl1):
    """Esta funcion le ayuda a acalcular el modulo de un numero complejo
        (tuple) --> float"""
    modulo = (((tpl1[0])**2) + ((tpl1[1])**2))**(1/2)
    return round(modulo,2)
#
def conjugado(tpl1):
    """ esta funcion le ayuda a calcular el conjugado de un numero complejo
        (tuple)--->tuple"""
    conjugado1 = tpl1[1] * -1
    return (tpl1[0],conjugado1)
#
def polaracartesiana(tpl):
    """ esta funcion le ayuda a pasar de coordenadas polares a coordenadas cartesianas
        (tuple) --> tupla"""
    angulo = math.radians(tpl[1])
    a = round(tpl[0] * math.cos(angulo),3)
    b = round(tpl[0] * math.sin(angulo),3)
    return (a,b)
#
def fase(tpl):
    """ esta funcion le ayuda a caluclar la fase un numero complejo
        (tuple) --> float"""
    return(round(math.atan(tpl[1]/tpl[0]),2))

###
def sumvectores(v,w):
    """esta funcion le ayuda a sumar dos vectores que tengan numeros complejos
        (list1d,list1d)---> list1d"""
    suma = []
    try:
        if len(v) == len(w):
            for i in range(len(v)):
                suma.append(sumar(v[i],w[i]))
            return suma
        else:
            raise ArithmeticError
    except ArithmeticError:
        print("Error longitud de matrices")

def auxinverso(a):
    """Esta funcion le ayuda a calcular el inverso de un numero complejos"""
    return (a[0] * (-1),a[1] * (-1))
def inverso(v):
    """Esta funcion le ayuda a calcular el inverso de un vector
        (list1d)--> list(1d)"""
    inverso = []
    for i in range(len(v)):
        inverso.append(auxinverso(v[i]))
    return inverso
# matrices
def multiplicacionescalar(v,c):
    """esta funcion le ayuda a multiplicar un  escalar por un vector
        (list1d)--->list1d"""
    multesc = []
    for i in range(len(v)):
        multesc.append(multiplicar(v[i],c))
    return multesc
#
def sumamtrices(v,w):
    """Esta funcion le ayuda a sumar dos matrices con numeros complejos
        (list2d,list2d)-->list2d)"""
    try:
        if len(v) == len(w) and (len(v[0]) == len(w[0])):
            suma = []
            for i in range(len(v)):
                filas = []
                for j in range(len(w[i])):
                    filas.append(sumar(v[i][j],w[i][j]))
                suma.append(filas)
            return suma
        else:
           raise ArithmeticError
    except ArithmeticError:
        print("error")

#
def inversaaditiva(w):
    """Funcion que le ayuda a calcular la inversa aditiva de una matriz compleja
        (list2d)--->list2d"""
    inversa = [[[] for j in range(len(w))]for i in range(len(w))]
    for i in range(len(w)):
        for j in range(len(w[i])):
            inversa[i][j] = multiplicar(w[i][j],[-1,0])
    return inversa
#
def multescalarm(w,c):
    """Funcion que le ayuda a calcular la multiplicación de un escalar por una matriz compleja
    (list2d),(tuple)"""
    resp = []
    for i in range(len(w)):
        resp.append([])
        for j in range(len(w[i])):
            resp[i].append(multiplicar(c, w[i][j]))
    return resp

#
def transpuesta(Mat):
    """Funcion que calcula la transpuesta de una matriz compleja
       (list2d) ---> list2d"""
    trans=[]
    for y in range(len(Mat[0])):
        trans.append([])
        for x in range(len(Mat)):
            trans[y].append(Mat[x][y])
    return trans
#
def conjugadamatriz(w):
    """Esta función le ayuda a calcular la conjugada de una matriz
        (list2d)---> list2d"""
    conju = []
    for i in range(len(w)):
        conju.append([])
        for j in range(len(w[0])):
            conju[i].append(conjugado(w[i][j]))
    return conju
#
def dagamatriz(w):
    """Esta funcion le ayuda a calcular la daga de una matriz
        (list2d) --> list(2d)"""
    conju = conjugadamatriz(w)
    return transpuesta(conju)
#
def validarmatrizmulti(m1, m2):
    if len(m1[0]) == len(m2):
        return True
    else:
        return False
#
def multiplimatr(v,u):
    """Funcion que calcula y valida dos matrices para multiplicar
        (list2d,list2d)--->list2d"""
    validador = validarmatrizmulti(v,u)
    try:
        if validador == True:
            multi = [[[0, 0] for j in range(len(u[0]))] for i in range(len(v))]
            for i in range(len(v)):
                for j in range(len(u[0])):
                    for k in range(len(v[0])):
                        multi[i][j] = sumar(multi[i][j], multiplicar(v[i][k], u[k][j]))
            return multi
        else:
            raise ArithmeticError
    except ArithmeticError:
        print("Error longitud de matrices")
#
def accion(ma,vec):
        """Funcion que le ayuda a calcular la "accion" de una matriz sobre una vector
        (list) ---> list"""
        row, col = len(ma), len(ma[0])
        length = len(vec)
        if (col == length):
            answ = [[0, 0] for x in range(row)]
            for i in range(row):
                for j in range(col):
                    mult = multiplicar(ma[i][j], vec[j])
                    answ[i] = sumar(answ[i], mult)
            return answ
        print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
#
def innerpro(vec1,vec2):
    """Esta funcion le ayuda a calcular el producto interno entres dos vectores
        (list1d,list1d)---->list1d"""
    try:
        if len(vec1) == len(vec2):
            resp = (0,0)
            for i in range(len(vec1)):
                resp = sumar(resp,multiplicar(vec1[i],vec2[i]))
            return resp
        else:
            raise ArithmeticError
    except ArithmeticError:
        print("Error en la longitud de vectores")
#
def norma(vect):
    """Esta funcion le ayuda a calular la norma de un vector
        (list1d) --> float"""
    norm = 0
    for i in range(len(vect)):
        norm += (modulo(vect[i]) ** 2)
    return round(math.sqrt(norm), 2)
#
def distancia(v1,v2):
    """Funcion que le ayuda a calcuñar la distancia entre dos vectores
        (list1d,list1d)--->float"""
    vectorsum = []
    for i in range(len(v1)):
        vectorsum.append(sumar(v1[i], v2[i]))
    return norma(vectorsum)
#
def unitaria(w):
    """Funcion que le ayuda a validar si una matriz es unitaria
        (list2d) ---> bool """
    uni = [[(0,0) for x in range(len(w[0]))]for y in range(len(w))]
    if len(w)!=len(w[0]):
        return False
    for i in range(len(w[0])):
        uni[i][i] = (1,0)
    m = multiplimatr(w,w)
    return (uni==m)
#
def hermitiana(w):
    """Funcion que valida si una matriz es hermitiana
        (list2d) --> bool"""
    adjcopi = dagamatriz(w)
    valiadador = True
    for i in range(len(w)):
        for j in range(len(w[0])):
            if w[i][j] == adjcopi[i][j] and w[i][j] == adjcopi[i][j]:
                continue
            else:
                valiadador = False
    return valiadador
#
def tensor(matrix1, matrix2):
    fil1, col1 = len(matrix1), len(matrix1[0])
    fil2, col2 = len(matrix2), len(matrix2[0])
    size = fil1 * fil2
    if (type(matrix1[0][0]) is int and type(matrix2[0][0]) is int):
        answ = []
        pos = 0
        for i in range(fil1):
            for j in range(fil2):
                answ.append(multiplicar(matrix1[i], matrix2[j]))
        return answ


    elif ((fil1 == col1) and (fil2 == col2)):

        answ = []
        column = 0
        for x in range(fil1):
            for y in range(fil2):
                row = []
                for z in range(col1):
                    row += multiplicacionescalar(matrix2[y][:], matrix1[x][z][:])

                answ.append(row)

        return answ

#

#print(tensor([[(0,1),(1,0)],[(1,1),(2,0)]],[(1,0),(0,1)]))

