# -*- coding: utf-8 -*-
from automatasComun import cambiarEstado,reducirConModulo, simetria
import numpy as np
"""
Created on Thu Apr 23 21:32:18 2020

@author: ignac
"""
def dibujarAutomataGeneradorDeslizadores(x0,y0,NumeroCuadranteAlQueApunta):
    x0,y0 = reducirConModulo(x0, y0)
    ejeY,ejeX=21,6            
    
    puntosVivos =[(0,5), (0,6), (1,5), (1,6), (5,3), (5,4), (10,2),
                  (10,3), (10,7), (10,8), (11,3), (11,4), (11,5), (11,6),
                  (11,7), (12,3), (12,4), (12,6), (12,7), (13,3), (13,4),
                  (13,6), (13,7), (14,4), (14,5), (14,6), (22,3), (23,2),
                  (23,3), (23,4), (24,1), (24,2), (24,3), (24,4), (24,5),
                  (25,0), (25,2), (25,4), (25,6), (26,0), (26,1), (26,5),
                  (26,6), (29,3), (30,2), (30,4), (31,2), (31,4), (32,3),
                  (33,3), (33,4), (34,3), (34,4), (35,3), (35,4)]
    
    if NumeroCuadranteAlQueApunta == 3:
        puntosVivos = simetria(puntosVivos, ejeY, ejeX,True,False)
        
    elif NumeroCuadranteAlQueApunta == 1:
        puntosVivos = simetria(puntosVivos, ejeY, ejeX,False,True)
        
    elif NumeroCuadranteAlQueApunta == 2:
        puntosVivos = simetria(puntosVivos, ejeY, ejeX,True,True)
   
    else:
        puntosVivos = simetria(puntosVivos, ejeY, ejeX,False, False)
    
    for x, y in puntosVivos:
        cambiarEstado(x0 +x, y0 +y, 1)
    pass


    

            
    
        

