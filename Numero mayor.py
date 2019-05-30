# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:39:51 2018

@author: luisl
"""

print("Adivinar cual es el numero mayor");

a=int(input("Ingrese el numero A: "))
b=int(input("Ingrese el numero B: "))
c=int(input("Ingrese el numero C: "))

if a>b and a>c:
    print("A es el mayor")
elif b>a and b>c:
    print("B es mayor")
elif c>a and c>b:
    print("C es mayor")
else:
    print("A, B y C son iguales")

