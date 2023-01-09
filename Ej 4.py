# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:41:07 2023

@author: Usuario
"""
def usarlafuerza(objetos):
    n = 0
    for i in objetos:
        if objetos[i] == "lightsaber": 
            print("Encontró el arma tras ", n, " intentos")
            break
        else:
            n = n+1
        print("No se encontró la espada")
            