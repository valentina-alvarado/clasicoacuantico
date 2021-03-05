#valentina alvarado
#libreria de los clasico a lo cuantico


from vectoresmatricescomplejos import *
import matplotlib.pyplot as plt
import numpy as np

# validación experimento con coeficientes booleanos
def validarbool(tpl):
    """ valida que los valores de una matriz sean de tipo booleano
        (list2d) ---> bool"""
    if tpl[0] == 0 or tpl[0] == 1:
        return True
    else:
        return False
def validarmtrbool(matriz):
    """Valida que los elementos de la matriz de un experimento de canicas clasico sean booleanos
        (list2d) -->bool"""
    validador = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if validarbool(matriz[i][j]):
                validador = True
            else:
                return False
    return validador
# libreria
def experimentobooleano(matriz,vectori,clicks):
    """Funcion que calcula y genera el estado del sistema despues de n clicks
        (list2d,list,int)--->(list)"""
    if validarmtrbool(matriz):
        if type(clicks) == int and clicks >=0:
            for i in range(1,clicks):
                vectori = accion(matriz,vectori)
            resp = accion(matriz,vectori)
            return resp
        return vectori
    else:
        return TypeError
#
def sistemaprobabilistico(matriz, vectori, clicks):
    """Funcion que calcula el sistema probabilistico clasico
        (list2d,list,int)-->list"""
    if type(clicks) == int and clicks >=0:
        for i in range(1,clicks):
            vectori = accion(matriz,vectori)
        resp = accion(matriz,vectori)
        return resp
    return vectori
#
def sistemaprobabicuantico(matriz,clicks):
    """Funcion que calcula el sistema probabilistico cuantico
        (list2d,list,int)-->list"""
    if type(clicks) == int and clicks >= 0:
        for i in range(clicks):
            matrizmu = multiplimatr(matriz,matriz[:])
        #
        for k in range(len(matrizmu)):
            fila = []
            for j in range(len(matrizmu[i])):
                fila.append([modulo(matrizmu[k][j])**2])
            matriz[k] = fila
        return matriz
    else:
        ArithmeticError
#
def multiplesrendijascu(matriz,clicks):
    """Funcion que calcula el sistema probabilistico clasico de multiples rendijas
          (list2d,list,int)-->list"""
    return sistemaprobabicuantico(matriz,clicks)
#
def multiplesrendijascla(matriz,vectori,clicks):
    """""Funcion que calcula el sistema probabilistico cuantico de multiples rendijas
          (list2d,list,int)-->list"""
    return sistemaprobabilistico(matriz,vectori,clicks)
#
def graficaprobabilidades(vector):
    """Funcion que grafica con un diagrama de barras la probabilidad de un vector de estados
        (list) --> grafica"""
    plt.bar(range(len(vector)), vector, color='red')
    plt.title("probabilidades de un estado")
    plt.show()


graficaprobabilidades([0.15925925925925927,0,0.05925925925925925,1.8833333333333333,0.5888888888888889,0.13333333333333333,0.14814814814814814,0.26388888888888884])