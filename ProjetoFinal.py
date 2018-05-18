# -*- coding: utf-8 -*-
"""
Created on Thu May 10 18:57:17 2018

@author: abrahao de weber
"""

import pygame
import sys
from pygame.locals import *
import random




#sys.path.append('./data')

janela = pygame.display.set_mode((1200, 500), 0, 32)
pygame.display.set_caption('Batalha Naval')
imagem = pygame.image.load("batalhateste.png").convert()
imagem2 = pygame.image.load("batalhateste.png").convert()
water = pygame.image.load("agua.png").convert()
img_botao = pygame.image.load("botao.png").convert()
preto = pygame.image.load("preto.png").convert()



coord = [731,28]
quadrado = [44,44]

coord1 = [221,28]

tam_navio = [[44,40,1],[88,40,2],[132,40,3],[176,40,4]]
coord_navio = [[18,8,0],[18,70,0],[18,176,0],[118,8,0]]
rotate_navio = []
navio1 = pygame.image.load("navio1.png").convert()
navio2 = pygame.image.load("navio2.png").convert()
navio3 = pygame.image.load("navio3.png").convert()
navio4 = pygame.image.load("navio4.png").convert()
ready = pygame.image.load("ready.png").convert()
navio1 = pygame.transform.rotate(navio1, 270)
navio2 = pygame.transform.rotate(navio2, 270)
navio3 = pygame.transform.rotate(navio3, 270)
navio4 = pygame.transform.rotate(navio4, 270)
listanavionr = [navio1,navio2,navio3,navio4]
listanavio = [navio1,navio2,navio3,navio4]

oponente=[]

voce=[]



def Game():
    for i in range(10):
        voce.append([])
        oponente.append([])
        for j in range(7):
            oponente[-1].append(0)
            voce[-1].append(0)
    global listanavio
    global navio4
    mousepressed_up = [False,-1]
    i = 1
    readylista = []
    while True:
        clicou = False
        janela.blit(imagem, (180, 0))
        janela.blit(imagem2,(690,0))
        janela.blit(preto, (0,0))
        janela.blit(ready, (9, 369))
        
        xx,yy = pygame.mouse.get_pos()
        #print(xx,yy)
        if mousepressed_up[0] and listanavio[mousepressed_up[1]] not in readylista:
            coord_navio[mousepressed_up[1]]=[xx,yy,coord_navio[mousepressed_up[1]][2]]
            
            
                
        for event in pygame.event.get():
            for i in range(len(coord_navio)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicou = True
                    if xx > coord_navio[i][0] and xx < coord_navio[i][0] + tam_navio[i][1] and yy > coord_navio[i][1] and yy < coord_navio[i][1] + tam_navio[i][0]:
                        mousepressed_up=[True,i]
                        
                        
                if event.type == pygame.MOUSEBUTTONUP:
                    mousepressed_up=[False,mousepressed_up[1]]

                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT and listanavio[mousepressed_up[1]] not in readylista:
                    old=tam_navio[mousepressed_up[1]][0]
                    tam_navio[mousepressed_up[1]][0] = tam_navio[mousepressed_up[1]][1]
                    
                    tam_navio[mousepressed_up[1]][1] = old
                    
                    coord_navio[mousepressed_up[1]][2]+=90
                    
                    
                    listanavio[mousepressed_up[1]] = pygame.transform.rotate(listanavionr[mousepressed_up[1]],coord_navio[mousepressed_up[1]][2])
                        
           
            
            
            
            
            
            
            
            
            
        for i in range(len(coord_navio)):
             janela.blit(listanavio[i], (coord_navio[i][0],coord_navio[i][1]))
                    
                
        for i in range(10):
            for x in range(7):
                if xx > coord[0]+(i)*quadrado[0] and yy > coord[1] + (x)*quadrado[1]  and xx < coord[0]+(i+1)*quadrado[0] and yy < coord[1] + (x+1)*quadrado[1]:
                    janela.blit(img_botao,(coord[0]+(i)*quadrado[0],coord[1]+(x)*quadrado[1]))
                    
                    
                    
        for i in range(10):
            for x in range(7):
                if clicou:
                    
                    if xx > 9 and xx < 139 and yy > 369 and yy < 419:
                        if coord_navio[mousepressed_up[1]][0] > coord1[0]+(i)*quadrado[0] and coord_navio[mousepressed_up[1]][1] > coord1[1] + (x)*quadrado[1]  and coord_navio[mousepressed_up[1]][0] <= coord1[0]+(i+1)*quadrado[0] and coord_navio[mousepressed_up[1]][1] <= coord1[1] + (x+1)*quadrado[1]:
                            #print("teste")
                            coord_navio[mousepressed_up[1]][0] = coord1[0] + (i)*quadrado[0]
                            coord_navio[mousepressed_up[1]][1] = coord1[1] + (x)*quadrado[0]
                            readylista.append(listanavio[mousepressed_up[1]])
                            for g in range(tam_navio[mousepressed_up[1]][2]):
                                if tam_navio[mousepressed_up[1]][1] == 40:
                                    voce[i+g][x] = 1
                                if tam_navio[mousepressed_up[1]][0] == 40:
                                    voce[i][x+g] = 1
                            print(voce)
                        
                        
        clicou = False
        
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
                            				    
					
        pygame.display.update()
Game()



        
                        
                        
            
            
            
            