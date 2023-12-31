'''
Una vez creado todo el código, descubrí varios tipos de patrones en internet que no desaparecen y se mueven de forma continua, 
con las posibilidades de mi ordenador (ya que se congela si hay mucha información o dura demasiado), he conseguido que interactuen
varios de estos y se finalize la simulación de forma rápida y bonita.
'''

import numpy as np
import pygame
import time
pygame.init()

#Pequeña pantalla de simulación
whidth, height = 1000, 1000
screen = pygame.display.set_mode((height,whidth))

#Tamaño de los cuadrados
nxC, nyC = 25, 25

dimCW = whidth / nxC
dimCH = height / nyC


#Estado de las celdas Vivas = 1; Muertas = 0
gamestate = np.zeros((nxC, nyC))

bg = 25, 25, 25
screen.fill(bg)
#Nave
gamestate[17, 12] = 1
gamestate[17, 10] = 1
gamestate[18, 13] = 1
gamestate[19, 13] = 1
gamestate[20, 13] = 1
gamestate[20, 10] = 1
gamestate[21, 13] = 1
gamestate[21, 12] = 1
gamestate[21, 11] = 1

#Palo
gamestate[13,12] = 1
gamestate[13,13] = 1
gamestate[13,11] = 1
#Móvil 2
gamestate[4,5] = 1
gamestate[5,3] = 1
gamestate[5,5] = 1
gamestate[6,4] = 1
gamestate[6,5] = 1

#Móvil 1
gamestate[20,5] = 1 
gamestate[20,4] = 1 
gamestate[21,5] = 1 
gamestate[21,3] = 1
gamestate[22,5] = 1

while True:

    #manejamos el error de cálculo al utilizar datos no actualizados
    newgamestate = np.copy(gamestate)

    screen.fill(bg)

    time.sleep(0.1)

    for y in range(0, nxC):
        for x in range(0, nyC):

            #Calculamos el número de vecinos cercanos y modulamos para atravesar paredes
            n_neigh = gamestate[(x-1) % nxC, (y-1) % nyC] + \
                      gamestate[(x)   % nxC, (y-1) % nyC] + \
                      gamestate[(x+1) % nxC, (y-1) % nyC] + \
                      gamestate[(x+1) % nxC, (y)   % nyC] + \
                      gamestate[(x+1) % nxC, (y+1) % nyC] + \
                      gamestate[(x)   % nxC, (y+1) % nyC] + \
                      gamestate[(x-1) % nxC, (y+1) % nyC] + \
                      gamestate[(x-1) % nxC, (y)   % nyC]

            #Si hay tres vecinas vivas, revive
            if gamestate[x,y] == 0 and n_neigh == 3:
                newgamestate[x,y] = 1       
            
            #Si tiene menos de dos o más de tres vecinas vivas, muere
            elif gamestate[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newgamestate[x,y] = 0
            
            #Dibujo de cada celda
            poly = [((x)   * dimCW, (y) * dimCH),
                  ((x+1) * dimCW,   (y) * dimCH),
                  ((x+1) * dimCW, (y+1) * dimCH),
                  ((x)   * dimCW, (y+1) * dimCH),]
            
            if newgamestate[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (20, 50, 30), poly, 0) #20, 50, 30  255, 255, 255
    pygame.display.flip()
    
    #Nuevo estado
    gamestate = np.copy(newgamestate)






