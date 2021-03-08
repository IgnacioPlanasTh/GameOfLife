# -*- coding: utf-8 -*-
from automatasComun import cambiarEstado,reducirConModulo
"""
Created on Thu Apr 23 15:39:55 2020

@author: Ignacio Planas
"""

def dibujarAutomataMovilArribaIzda(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0-1, y0-1, 1)
    cambiarEstado(x0  , y0-1, 1)
    cambiarEstado(x0+1, y0-1, 1)
    cambiarEstado(x0-1, y0  , 1)
    cambiarEstado(x0  , y0+1, 1)
    pass

def dibujarAutomataMovilArribaDcha(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)        
    cambiarEstado(x0-1, y0-1, 1)
    cambiarEstado(x0  , y0-1, 1)
    cambiarEstado(x0+1, y0-1, 1)
    cambiarEstado(x0+1, y0  , 1)
    cambiarEstado(x0  , y0+1, 1)
    pass


def dibujarAutomataMovilAbajoIdza(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)
            
    cambiarEstado(x0-1, y0+1, 1)
    cambiarEstado(x0  , y0+1, 1)
    cambiarEstado(x0+1, y0+1, 1)
    cambiarEstado(x0-1, y0  , 1)
    cambiarEstado(x0  , y0-1, 1)
    pass

def dibujarAutomataMovilAbajoDcha(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)  
            
    cambiarEstado(x0-1, y0+1, 1)
    cambiarEstado(x0  , y0+1, 1)
    cambiarEstado(x0+1, y0+1, 1)
    cambiarEstado(x0+1, y0  , 1)
    cambiarEstado(x0  , y0-1, 1)
    pass
    


def dibujar4AutomatasMoviles(x0,y0):
    x0,y0 =reducirConModulo(x0, y0)
    for y in range(y0-4, y0 +5):
        for x in range(x0 -4, x0 +5):
            cambiarEstado(x, y, 0)
            
    dibujarAutomataMovilArribaIzda(x0 -3, y0 -3)
    dibujarAutomataMovilArribaDcha(x0 +3, y0 -3)
    dibujarAutomataMovilAbajoIdza(x0 -3, y0 +3)
    dibujarAutomataMovilAbajoDcha(x0 +3, y0 +3)
    pass

def dibujarAutomataMovilVertical(x0,y0, reverse=False):
    x0,y0 =reducirConModulo(x0, y0) 
    for y in range(y0, y0 +5):
        for x in range(x0, x0 +4):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0   , y0 +2, 1)
    cambiarEstado(x0 +1, y0 +1, 1)
    cambiarEstado(x0 +1, y0 +2, 1)
    cambiarEstado(x0 +1, y0 +3, 1)
    cambiarEstado(x0 +2, y0   , 1)
    cambiarEstado(x0 +2, y0 +1, 1)
    cambiarEstado(x0 +2, y0 +3, 1)
    cambiarEstado(x0 +2, y0 +4, 1)
    cambiarEstado(x0 +3, y0 +2, 1)
    
    if not reverse:
        cambiarEstado(x0   , y0 +3, 1)
        cambiarEstado(x0 +1, y0 +4, 1)
        cambiarEstado(x0 +3, y0 +1, 1)
    else:
        cambiarEstado(x0   , y0 +1, 1)
        cambiarEstado(x0 +1, y0   , 1)
        cambiarEstado(x0 +3, y0 +3, 1)
    pass

def dibujarAutomataMovilVerticalGrande(x0,y0,reverse=False):
    x0,y0 =reducirConModulo(x0, y0)

    for x in range(x0, x0 +4):
            cambiarEstado(x, y0 +5, 0)
    dibujarAutomataMovilVertical(x0, y0, reverse)
    if not reverse:
        cambiarEstado(x0  , y0 +4, 1)
        cambiarEstado(x0 +1, y0 +5, 1)
        cambiarEstado(x0 +2, y0 +5, 1)
    else:
        cambiarEstado(x0   , y0 +1, 1)
        cambiarEstado(x0 +1, y0   , 1)
        cambiarEstado(x0 +2, y0   , 1)
    pass
        

def dibujarAutomataMovilHorizontal(x0,y0, reverse=False):
    x0,y0 =reducirConModulo(x0, y0) 
    for y in range(y0, y0 +4):
        for x in range(x0, x0 +5):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0   , y0 +2, 1)
    cambiarEstado(x0 +1, y0 +1, 1)
    cambiarEstado(x0 +1, y0 +2, 1)
    cambiarEstado(x0 +2, y0   , 1)
    cambiarEstado(x0 +2, y0 +1, 1)
    cambiarEstado(x0 +2, y0 +3, 1)
    cambiarEstado(x0 +3, y0 +1, 1)
    cambiarEstado(x0 +3, y0 +2, 1)
    cambiarEstado(x0 +4, y0 +2, 1)
    if not reverse:
        cambiarEstado(x0   , y0 +1, 1)
        cambiarEstado(x0 +1, y0   , 1)
        cambiarEstado(x0 +3, y0 +3, 1)
    else:
        cambiarEstado(x0 +1, y0 +3, 1)
        cambiarEstado(x0 +3, y0   , 1)
        cambiarEstado(x0 +4, y0 +1, 1)
            
def dibujarAutomataMovilHorizontalGrande(x0,y0, reverse=False):
    x0,y0 =reducirConModulo(x0, y0)
    for y in range(y0, y0+4):
        for x in range( x0, x0 +6):
            cambiarEstado(x0 +5, y, 0)
    dibujarAutomataMovilHorizontal(x0 +1, y0,reverse)
    if not reverse:
        cambiarEstado(x0 +1, y0   , 1)
        cambiarEstado(x0   , y0 +1, 1)
        cambiarEstado(x0   , y0 +2, 1)
    else:
        cambiarEstado(x0 +5, y0   , 1)
        cambiarEstado(x0 +6, y0 +1, 1)
        cambiarEstado(x0 +6, y0 +2, 1)
        