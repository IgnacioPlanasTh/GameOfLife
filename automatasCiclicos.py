# -*- coding: utf-8 -*-
from automatasComun import cambiarEstado,reducirConModulo
"""
Created on Thu Apr 23 15:46:18 2020

@author: Ignacio Planas
"""

def dibujarAutomataPalo10(x0, y0, vertical = True):
    x0,y0 = reducirConModulo(x0, y0)
    for i in range(0,10):
        if vertical:
            cambiarEstado(x0, y0 +i, 1)
        else:
            cambiarEstado(x0 +i, y0, 1)
    pass   

def dibujarAutomataPalo3(x0,y0,vertical=True):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0, y0, 1)
    if not vertical:
        cambiarEstado(x0+1, y0, 1)
        cambiarEstado(x0-1, y0, 1)
    else:
        cambiarEstado(x0, y0+1, 1)
        cambiarEstado(x0, y0-1, 1)
    pass

def dibujarAutomataEscarabajo(x0,y0):
     x0,y0 = reducirConModulo(x0, y0)
     for y in range(y0-6,y0+7):
        for x in range(x0-6,x0+7):
            cambiarEstado(x, y, 0) 
     dibujarAutomataPalo3(x0 -3, y0 +1, False)
     dibujarAutomataPalo3(x0 -3, y0 -1, False)
     dibujarAutomataPalo3(x0 +3, y0 +1, False)
     dibujarAutomataPalo3(x0 +3, y0 -1, False)
     
     dibujarAutomataPalo3(x0 -1, y0 +3)
     dibujarAutomataPalo3(x0 -1, y0 -3)
     dibujarAutomataPalo3(x0 +1, y0 +3)
     dibujarAutomataPalo3(x0 +1, y0 -3)
     
     
     dibujarAutomataPalo3(x0 -3, y0 -6, False)
     dibujarAutomataPalo3(x0 -3, y0 +6, False)
     dibujarAutomataPalo3(x0 +3, y0 -6, False)
     dibujarAutomataPalo3(x0 +3, y0 +6, False)
     
     dibujarAutomataPalo3(x0 -6, y0 -3)
     dibujarAutomataPalo3(x0 -6, y0 +3)
     dibujarAutomataPalo3(x0 +6, y0 -3)
     dibujarAutomataPalo3(x0 +6, y0 +3)
     pass
    
def dibujarAutomataFlor(x0,y0,reverse=False):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-1,y0+2):
        for x in range(x0-1,x0+2):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0 -1, y0, 1)
    cambiarEstado(x0   , y0, 1)
    cambiarEstado(x0 +1, y0, 1)
    
    if not reverse:
        cambiarEstado(x0 -1, y0 -1, 1)
        cambiarEstado(x0 +1, y0 -1, 1)
        cambiarEstado(x0   , y0 +1, 1)
        
    else:
        cambiarEstado(x0 -1, y0 +1, 1)
        cambiarEstado(x0 +1, y0 +1, 1)
        cambiarEstado(x0   , y0 -1, 1)
    pass

def dibujarAutomataRana(x0,y0,reverse=False):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0-3, y0+4):
        for x in range(x0-2, x0+3):
            cambiarEstado(x, y, 0)
    
    cambiarEstado(x0, y0 -2, 1)
    cambiarEstado(x0, y0 +2, 1)
    
    if not reverse:
        cambiarEstado(x0 +1, y0 -1, 1)
        cambiarEstado(x0 +1, y0   , 1)
        cambiarEstado(x0 +1, y0 +1, 1)
        cambiarEstado(x0 +2, y0 -1, 1)
        cambiarEstado(x0 +2, y0   , 1)
        cambiarEstado(x0 +2, y0 +1, 1)
        
        
        cambiarEstado(x0 -2, y0 -2, 1)
        cambiarEstado(x0 -2, y0 -3, 1)
        
        cambiarEstado(x0 -2, y0 +2, 1)
        cambiarEstado(x0 -2, y0 +3, 1)
    else:
        cambiarEstado(x0 -1, y0 -1, 1)
        cambiarEstado(x0 -1, y0   , 1)
        cambiarEstado(x0 -1, y0 +1, 1)
        cambiarEstado(x0 -2, y0 -1, 1)
        cambiarEstado(x0 -2, y0   , 1)
        cambiarEstado(x0 -2, y0 +1, 1)
        
        
        cambiarEstado(x0 +2, y0 -2, 1)
        cambiarEstado(x0 +2, y0 -3, 1)
        
        cambiarEstado(x0 +2, y0 +2, 1)
        cambiarEstado(x0 +2, y0 +3, 1)
    pass
    
def dibujarNoria(x0,y0):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0, y0 +8):
        for x in range(x0, x0 +8):
            cambiarEstado(x, y, 0)
            
    cambiarEstado(x0   , y0 +4, 1)
    cambiarEstado(x0 +1, y0 +4, 1)
    
    cambiarEstado(x0 +3, y0   , 1)
    cambiarEstado(x0 +3, y0 +1, 1)
    
    cambiarEstado(x0 +6, y0 +3, 1)
    cambiarEstado(x0 +7, y0 +3, 1)
    
    cambiarEstado(x0 +4, y0 +6, 1)
    cambiarEstado(x0 +4, y0 +7, 1)
    
    cambiarEstado(x0 +1, y0 +2, 1)
    
    cambiarEstado(x0 +2, y0 +6, 1)
    
    cambiarEstado(x0 +5, y0 +1, 1)
    
    cambiarEstado(x0 +6, y0 +5, 1)
    pass

def dibujarTortuga(x0, y0, reverse = False):
    x0,y0 = reducirConModulo(x0, y0)
    for y in range(y0, y0 +6):
        for x in range(x0, x0 +7):
            cambiarEstado(x, y, 0)
    cambiarEstado(x0 +2, y0 +1, 1)
    cambiarEstado(x0 +2, y0 +2, 1)
    cambiarEstado(x0 +2, y0 +3, 1)
    cambiarEstado(x0 +2, y0 +4, 1)
    
    cambiarEstado(x0 +4, y0 +1, 1)
    cambiarEstado(x0 +4, y0 +2, 1)
    cambiarEstado(x0 +4, y0 +3, 1)
    cambiarEstado(x0 +4, y0 +4, 1)
    
    cambiarEstado(x0 +1, y0   , 1)
    cambiarEstado(x0 +1, y0 +5, 1)
    
    cambiarEstado(x0 +5, y0   , 1)
    cambiarEstado(x0 +5, y0 +5, 1)
    if not reverse:
        cambiarEstado(x0   , y0 +3, 1)
        cambiarEstado(x0   , y0 +4, 1)
        cambiarEstado(x0   , y0 +5, 1)
        cambiarEstado(x0 +6, y0 +3, 1)
        cambiarEstado(x0 +6, y0 +4, 1)
        cambiarEstado(x0 +6, y0 +5, 1)
        
        cambiarEstado(x0 +1, y0 +1, 1)
        cambiarEstado(x0 +2, y0   , 1)
        cambiarEstado(x0 +4, y0   , 1)
        cambiarEstado(x0 +5, y0 +1, 1)
    else:
        cambiarEstado(x0   , y0   , 1)
        cambiarEstado(x0   , y0 +1, 1)
        cambiarEstado(x0   , y0 +2, 1)
        cambiarEstado(x0 +6, y0   , 1)
        cambiarEstado(x0 +6, y0 +1, 1)
        cambiarEstado(x0 +6, y0 +2, 1)
        
        cambiarEstado(x0 +1, y0 +4, 1)
        cambiarEstado(x0 +2, y0 +5, 1)
        cambiarEstado(x0 +4, y0 +5, 1)
        cambiarEstado(x0 +5, y0 +4, 1)
    pass
        