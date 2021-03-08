# -*- coding: utf-8 -*-
from automatasComun import cambiarEstado,reducirConModulo

"""
Created on Thu Apr 23 10:12:16 2020

@author: Ignacio Planas
"""   
def dibujarAutoomatainvomil8(x0,y0,reversed=False):   
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)
    
    cambiarEstado(x0 +1,y0, 1)
    cambiarEstado(x0 -1,y0, 1)
    cambiarEstado(x0,y0 +1, 1)
    cambiarEstado(x0,y0 -1, 1)
        
    if not reversed:
        cambiarEstado(x0+1, y0 -1, 1)
        cambiarEstado(x0-1, y0 +1, 1)
    else:
        cambiarEstado(x0+1, y0 +1, 1)
        cambiarEstado(x0-1, y0 -1, 1)
    pass



def dibujarCuadrado(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    cambiarEstado(x0   ,y0   , 1) 
    cambiarEstado(x0 +1,y0   , 1) 
    cambiarEstado(x0 +1,y0 +1, 1)
    cambiarEstado(x0   ,y0 +1, 1) 
    pass

    
def dibujarCuadradoInmovilGigante(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-7,y0+8):
        for x in range(x0-7,x0+8):
            cambiarEstado(x, y, 0)
            
    dibujarAutoomatainvomil8(x0-2, y0-2)
    dibujarAutoomatainvomil8(x0+2, y0-2,True)
    dibujarAutoomatainvomil8(x0+2, y0+2)
    dibujarAutoomatainvomil8(x0-2, y0+2,True)
        
    dibujarCuadrado(x0-6, y0-2)
    dibujarCuadrado(x0-6, y0+1)
    dibujarCuadrado(x0+5, y0-2)
    dibujarCuadrado(x0+5, y0+1)
        
    dibujarCuadrado(x0-2, y0-6)
    dibujarCuadrado(x0-2, y0+5)
    dibujarCuadrado(x0+1, y0-6)
    dibujarCuadrado(x0+1, y0+5)
    pass

def dibujarBarco(x0,y0, NumeroCuadranteAlQueApunta):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0 +1, y0 +1, 1)
    cambiarEstado(x0 +1, y0 -1, 1)
    cambiarEstado(x0 -1, y0 -1, 1)
    cambiarEstado(x0 -1, y0 +1, 1)
    if NumeroCuadranteAlQueApunta == 1:
        cambiarEstado(x0 +1, y0 -1, 1)
    elif NumeroCuadranteAlQueApunta == 3:
        cambiarEstado(x0 -1, y0 +1, 1)
    elif NumeroCuadranteAlQueApunta == 4:
        cambiarEstado(x0 +1, y0 +1, 1)
    else:
        cambiarEstado(x0 -1, y0 -1, 1)    
    pass

def dibujarCruz(x0,y0):
    for y in range(y0 -4, y0 +5):
        for x in range(x0 -4, x0 +5):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0 -2, y0 +1, 1)
    cambiarEstado(x0 -2, y0 -1, 1)
    cambiarEstado(x0 -3, y0 +1, 1)
    cambiarEstado(x0 -3, y0 -1, 1)
    cambiarEstado(x0 -4, y0   , 1)
    
    cambiarEstado(x0 +2, y0 +1, 1)
    cambiarEstado(x0 +2, y0 -1, 1)
    cambiarEstado(x0 +3, y0 +1, 1)
    cambiarEstado(x0 +3, y0 -1, 1)
    cambiarEstado(x0 +4, y0   , 1)
    
    cambiarEstado(x0 -1, y0 +2, 1)
    cambiarEstado(x0 -1, y0 +3, 1)
    cambiarEstado(x0   , y0 +4, 1)
    cambiarEstado(x0 +1, y0 +2, 1)
    cambiarEstado(x0 +1, y0 +3, 1)
    
    cambiarEstado(x0 -1, y0 -2, 1)
    cambiarEstado(x0 -1, y0 -3, 1)
    cambiarEstado(x0   , y0 -4, 1)
    cambiarEstado(x0 +1, y0 -2, 1)
    cambiarEstado(x0 +1, y0 -3, 1)
    pass