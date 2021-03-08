# -*- coding: utf-8 -*-
from atributos import nxC,nyC,gameState
"""
Created on Thu Apr 23 15:47:14 2020

@author: ignac
"""
def reducirConModulo(x0,y0):
    x0 = x0 % nxC
    y0 = y0 % nyC
    return x0,y0

def cambiarEstado( x0, y0, valor):
    x0,y0 = reducirConModulo(x0, y0)
    gameState[x0,y0] = valor

def simetria (listaPuntos, ejeY, ejeX, simetriaRespectoY=False, simetriaRespectoX=False):
    result =[]
    for x, y in listaPuntos:
        y0=y
        x0=x
        if simetriaRespectoY:
            x0 = ejeY + (ejeY-x)
            
        if simetriaRespectoX:
            y0 = ejeX + (ejeX-y)
        result.append((x0,y0))
    return result






# =============================================================================
# # importa la librería Pygame
# import pygame
# 
# 
# def main():
#     # inicializa Pygame
#     pygame.init()
# 
#     # establece el título de la ventana
#     pygame.display.set_caption(u'Eventos del teclado')
# 
#     # establece el tamaño de la ventana
#     pygame.display.set_mode((400, 400))
#     
# 
#     # bucle infinito
#     while True:
#         # obtiene un solo evento de la cola de eventos
#         event = pygame.event.wait()
# 
#         # si se presiona el botón 'cerrar' de la ventana
#         if event.type == pygame.QUIT:
#             # detiene la aplicación
#             break
# 
#         # captura los eventos 'KEYDOWN' y 'KEYUP'
#         if event.type in (pygame.KEYDOWN, pygame.KEYUP):
#             # obtiene el nombre de la tecla
#             key_name = pygame.key.name(event.key)
# 
#             # convierte el nombre de la tecla en mayúsculas
#             key_name = key_name.upper()
# 
#             # si alguna tecla es presionada
#             if event.type == pygame.KEYDOWN:
#                 # imprime en la consola la tecla presionada
#                 print(u'Tecla "{}" presionada'.format(key_name))
# 
#             # si alguna tecla es soltada
#             elif event.type == pygame.KEYUP:
#                 # imprime en la consola la tecla soltada
#                 print(u'Tecla "{}" soltada'.format(key_name))
# 
#     # finaliza Pygame
#     pygame.quit()
# 
# 
# if __name__ == '__main__':
#     main()
# =============================================================================
