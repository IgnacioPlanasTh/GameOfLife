# -*- coding: utf-8 -*-
import numpy as np

"""
Created on Thu Apr 23 13:41:44 2020

@author: Ignacio Planas
"""

# Definimos el numero de celdas
nxC,nyC=100,100

# Creamos la matriz de celulas. 0=muerta; 1=viva
gameState = np.zeros((nxC,nyC))
