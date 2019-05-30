# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:40:42 2018

@author: luisl
"""

from random import *
 
def generaNumeroAleatorio(minimo,maximo):
 
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
 
        return randint(minimo, maximo)
    except TypeError:
        print("Debes escribir numeros")
        return -1
 
numero_buscado = generaNumeroAleatorio(1,100)
 
encontrado = False
intentos = 0

while not encontrado:
    try:
        numero_usuario = int(input("Introduce el número buscado: "))
 
        if numero_usuario > numero_buscado:
            print("El número que buscas es menor")
            intentos = intentos +1
        elif numero_usuario < numero_buscado:
            print("El numero que buscas es mayor")
            intentos = intentos +1
        else:
            encontrado = True
            print("Has acertado el número correcto es " , numero_usuario, " te ha llevado ", intentos," intentos")
    except ValueError as err:
        print(err)