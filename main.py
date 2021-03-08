import pygame
import numpy as np
import time

import automatasFijos
import automatasCiclicos
import automatasMoviles
import automatasGeneradores

from atributos import gameState, nxC, nyC

pygame.init()
width, height = 1000,1000
screen= pygame.display.set_mode((height,width))

bg =25,25,25
#pinatmos el fondo con el color elegido
screen.fill(bg)

#dimensiones de las celdas
dimCW= width/nxC
dimCH = height/nyC

#Control de la ejecucion
pauseExect = True



# =============================================================================
#Inicializar los automatas
# automatasMoviles.dibujar4AutomatasMoviles(50, 50)
# automatasFijos.dibujarCuadradoInmovilGigante(50, 10)
# 
# automatasCiclicos.dibujarAutomataPalo10(50, 5)
# automatasCiclicos.dibujarAutomataEscarabajo(50, 80)
# automatasCiclicos.dibujarAutomataFlor(25, 50)
# automatasCiclicos.dibujarAutomataRana(75, 50)
# 
# automatasGeneradores.dibujarAutomataGeneradorDeslizadores(0,0,4)
# automatasGeneradores.dibujarAutomataGeneradorDeslizadores(57,57,2)
# 
# automatasFijos.dibujarCruz(50, 50)
# automatasCiclicos.dibujarNoria(0, 0)
# 
# for x in range(0,nxC-5,7):
#     for y in range(0,nyC-6,7):
#         if x % 14 == 0:
#             automatasMoviles.dibujarAutomataMovilVertical(x, y, True)
#         else:
#             automatasMoviles.dibujarAutomataMovilVertical(x, y)
# automatasFijos.dibujarCuadradoInmovilGigante(50, 50)
# automatasCiclicos.dibujarNoria(50, 50)
# automatasMoviles.dibujarAutomataMovilVerticalGrande(4,4)
# automatasCiclicos.dibujarTortuga(30, 30,True)
# automatasCiclicos.dibujarTortuga(50, 50)
# automatasMoviles.dibujarAutomataMovilHorizontal(50,50)
# automatasMoviles.dibujar4AutomatasMoviles(50, 50)
# automatasMoviles.dibujarAutomataMovilHorizontal(20, 2)
# automatasMoviles.dibujarAutomataMovilHorizontal(20, 52, True)
# automatasMoviles.dibujarAutomataMovilHorizontalGrande(10, 2)
# automatasMoviles.dibujarAutomataMovilHorizontalGrande(10, 52, True)
# =================================================== ==========================



#bucle de ejecucion
while True:
    newGameState = np.copy(gameState)
    
    time.sleep(0.1)
    
    
    
    #Registramos eventos del teclado y raton
    ev = pygame.event.get()
    
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect 
       
    mouseClick = pygame.mouse.get_pressed()
    if sum(mouseClick)>0:
        posX,posY = pygame.mouse.get_pos()
        celX,celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
        if mouseClick[2]==1:
            newGameState[celX,celY] = 0
        else:
            newGameState[celX,celY] = 1

    if not pauseExect:
        screen.fill(bg)
        for y in range(0,nyC):
            for x in range(0,nxC):    
                n_neigh =   gameState[(x-1) % nxC,(y-1) % nyC] + \
                            gameState[(x)   % nxC,(y-1) % nyC] + \
                            gameState[(x+1) % nxC,(y-1) % nyC] + \
                            gameState[(x-1) % nxC,(y)   % nyC] + \
                            gameState[(x+1) % nxC,(y)   % nyC] + \
                            gameState[(x-1) % nxC,(y+1) % nyC] + \
                            gameState[(x)   % nxC,(y+1) % nyC] + \
                            gameState[(x+1) % nxC,(y+1) % nyC] 
                            
                #  Rule #1: una celula con exactamente 3 celulas vivas vecinas, "Reviva"
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1
                    
                #  Rule #2 : Una celula viva con menos de dos o mas de tres celulas vecinas vivas, "muere"
                elif gameState[x,y] == 1 and (n_neigh<2 or n_neigh>3):
                    newGameState[x,y] = 0
        
    for y in range(0,nyC):
        for x in range(0,nxC):   
            #Creamos el poligono de cada celda a dibujar.
            poly =[((x)   * dimCW, (y)   * dimCH),
                       ((x+1) * dimCW, (y)   * dimCH),
                       ((x+1) * dimCW, (y+1) * dimCH),
                       ((x)   * dimCW, (y+1) * dimCH)] 
                      
            #dibujamos la celda para cada par de x e y  
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (0,0,0), poly, 0)
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
                
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)
    
    #Actualizamos el estado del juego
    gameState = np.copy(newGameState)
    pygame.display.flip()
    