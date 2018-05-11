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

janela = pygame.display.set_mode((1020, 333), 0, 32)
pygame.display.set_caption('Batalha Naval')
imagem = pygame.image.load("batalha.jpg").convert()
imagem2 = pygame.image.load("batalha.jpg").convert()
water = pygame.image.load("agua.png").convert()
img_botao = pygame.image.load("botao.png").convert()
coord = [551,28]
quadrado = [43,39]
unicolugar = False
atual = [0,0]
def Game():
    unicolugar = False  
    atual = [0,0]
    i = 1
    while True:
        janela.blit(imagem, (0, 0))
        janela.blit(imagem2,(510,0))
        xx,yy = pygame.mouse.get_pos()
        i = 1
        x = 1
        if unicolugar:
            janela.blit(water,(atual[0],atual[1]))
        while i < 11 and x < 9:
            if xx > coord[0]+(i-1)*quadrado[0] and yy > coord[1] + (x-1)*quadrado[1]  and xx < coord[0]+i*quadrado[0] and yy < coord[1] + x*quadrado[1]:
                janela.blit(img_botao,(coord[0]+(i-1)*quadrado[0],coord[1]+(x-1)*quadrado[1]))
            i += 1
            if i == 11:
                i = 1
                x += 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pox,poy = pygame.mouse.get_pos()
                if pox > coord[0] and poy > coord[1] and pox < coord[0]+quadrado[0] and poy < coord[1] + quadrado[1]:
                    unicolugar=True
                    atual=[coord[0],coord[1]]                        
                else:
                    pass#unicolugar=False                   				    
		
					
        pygame.display.update()
Game()


            