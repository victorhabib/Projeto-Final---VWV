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
quadrado = [44,40]
unicolugar = False
atual = [0,0]
def Game():
	unicolugar = False  
	atual = [0,0]
	while True:
		janela.blit(imagem, (0, 0))
		janela.blit(imagem2,(510,0))
        
		xx,yy = pygame.mouse.get_pos()
		if unicolugar:
			janela.blit(water,(atual[0],atual[1]))
		if xx > coord[0] and yy > coord[1] and xx < coord[0]+quadrado[0] and yy < coord[1] + quadrado[1]:
			 janela.blit(img_botao,(coord[0],coord[1]))      
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
        #550 30
		
					
		pygame.display.update()
Game()

