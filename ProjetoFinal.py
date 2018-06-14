# -- coding: utf-8 --
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
imagem = pygame.image.load("batalhateste.png").convert_alpha()
imagem2 = pygame.image.load("batalhateste.png").convert_alpha()
img_botao = pygame.image.load("botao.png").convert()
preto = pygame.image.load("preto.png").convert()
xis_image = pygame.image.load("x.png").convert()
xis_image_verde = pygame.image.load("x_verde.png").convert()
voce_ganhou = pygame.image.load("voce_ganhou.png").convert_alpha()
voce_perdeu = pygame.image.load("voce_perdeu.png").convert_alpha()
tentar_novamente = pygame.image.load("tentar.png").convert_alpha()
sair = pygame.image.load("sair.png").convert_alpha()


coord = [731,28]
quadrado = [44,44]

coord1 = [221,28]

tam_navio = [[44,40,1],[88,40,2],[132,40,3],[176,40,4]]
coord_navio = [[18,8,0],[18,70,0],[18,176,0],[118,8,0]]
rotate_navio = []
navio1 = pygame.image.load("navio1.png").convert_alpha()
navio2 = pygame.image.load("navio2.png").convert_alpha()
navio3 = pygame.image.load("navio3.png").convert_alpha()
navio4 = pygame.image.load("navio4.png").convert_alpha()
travar = pygame.image.load("travar.png").convert()
comecar = pygame.image.load("comecar.png").convert()
comecou_image = pygame.image.load("comecou.png").convert_alpha()
aviso_travar = pygame.image.load("travar_aviso.png").convert_alpha()

navio1 = pygame.transform.rotate(navio1, 270)
navio2 = pygame.transform.rotate(navio2, 270)
navio3 = pygame.transform.rotate(navio3, 270)
navio4 = pygame.transform.rotate(navio4, 270)
listanavionr = [navio1,navio2,navio3,navio4]
listanavio = [navio1,navio2,navio3,navio4]


oponente=[]

voce=[]

xis = []
xis2 = []

h = 0
    
contador_ganhar = 0    
contador = 0
turno = 0
listacomecar = 0
comecou = 0
xis_lista = []
oponente_lista = []
def Game():
    for i in range(10):
        voce.append([])
        oponente.append([])
        xis.append([])
        xis2.append([])
        for j in range(7):
            oponente[-1].append(0)
            voce[-1].append(0)
            xis[-1].append(0)
            xis2[-1].append(0)
    global listanavio
    global navio4
    global contador
    global turno
    global listacomecar
    global contador_ganhar
    global comecou
    global xis_lista
    global oponente_lista
    global h
    posicionou = False
    perdeu = False
    contador_rot = 0
    resultado = 0
    mousepressed_up = [False,-1]
    random_i=random.randint(0,9)
    random_x=random.randint(0,6)
    i = 1
    travarlista = []
    while True:

        clicoutravar = False
        clicoucomecar = False
        clicoubotao = False
        #Imagens de fundo
        janela.blit(preto, (0,0))
        janela.blit(imagem, (180, 0))
        janela.blit(imagem2,(690,0))
        
        janela.blit(travar, (9, 369))
        janela.blit(comecar, (230, 369))
        janela.blit(voce_ganhou,(300,500))

        
        xx,yy = pygame.mouse.get_pos()
        #print(xx,yy)
        #Condicao para clicar e arrastar o navio
        if mousepressed_up[0] and listanavio[mousepressed_up[1]] not in travarlista:
            coord_navio[mousepressed_up[1]]=[xx,yy,coord_navio[mousepressed_up[1]][2]]
            
            
        #Mouse no navio para poder clicar nele e arrastar
        for event in pygame.event.get():
            for i in range(len(coord_navio)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicoutravar = True
                    clicoucomecar = True
                    clicoubotao = True
                    clicounovamente = True
                    if xx > coord_navio[i][0] and xx < coord_navio[i][0] + tam_navio[i][1] and yy > coord_navio[i][1] and yy < coord_navio[i][1] + tam_navio[i][0]:
                        mousepressed_up=[True,i]
                        
                        
                if event.type == pygame.MOUSEBUTTONUP:
                    mousepressed_up=[False,mousepressed_up[1]]

                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    
                    
                    
                    
                    
                    
                    
                    
            #Girar o navio
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT and listanavio[mousepressed_up[1]] not in travarlista:
                    old=tam_navio[mousepressed_up[1]][0]
                    tam_navio[mousepressed_up[1]][0] = tam_navio[mousepressed_up[1]][1]
                    
                    tam_navio[mousepressed_up[1]][1] = old
                    
                    coord_navio[mousepressed_up[1]][2]+=90
                    
                    
                    listanavio[mousepressed_up[1]] = pygame.transform.rotate(listanavionr[mousepressed_up[1]],coord_navio[mousepressed_up[1]][2])
                        
           
            
            
            
            
            
            
            
            
        #Blitar o navio no lado
        for i in range(len(coord_navio)):
             janela.blit(listanavio[i], (coord_navio[i][0],coord_navio[i][1]))
                    
        
        for i in range(10):
            for x in range(7):
                #blita x no oponente
                if xis[i][x]:
                    janela.blit(xis_image, (coord[0]+(i)*quadrado[0], coord[1] + (x)*quadrado[1]))
                if xis[i][x] and oponente[i][x]:
                    janela.blit(xis_image_verde, (coord[0]+(i)*quadrado[0], coord[1] + (x)*quadrado[1]))
                #Blitar botoes do oponente
                if xx > coord[0]+(i)*quadrado[0] and yy > coord[1] + (x)*quadrado[1]  and xx < coord[0]+(i+1)*quadrado[0] and yy < coord[1] + (x+1)*quadrado[1]:
                    janela.blit(img_botao,(coord[0]+(i)*quadrado[0],coord[1]+(x)*quadrado[1]))

                    
                    
        #Criar matriz e definir, travar e definir coordenada do navio
        # matriz = coluna x linha
        for i in range(10):
            for x in range(7):
                if clicoutravar:
                    
                    if xx > 9 and xx < 206 and yy > 369 and yy < 419:
                        if coord_navio[mousepressed_up[1]][0] > coord1[0]+(i)*quadrado[0] and coord_navio[mousepressed_up[1]][1] > coord1[1] + (x)*quadrado[1]  and coord_navio[mousepressed_up[1]][0] <= coord1[0]+(i+1)*quadrado[0] and coord_navio[mousepressed_up[1]][1] <= coord1[1] + (x+1)*quadrado[1] and listanavio[mousepressed_up[1]] not in travarlista:
                            #print("teste")
                            coord_navio[mousepressed_up[1]][0] = coord1[0] + (i)*quadrado[0]
                            coord_navio[mousepressed_up[1]][1] = coord1[1] + (x)*quadrado[0]
                            travarlista.append(listanavio[mousepressed_up[1]])
                            for g in range(tam_navio[mousepressed_up[1]][2]):
                                if tam_navio[mousepressed_up[1]][1] == 40:
                                    voce[i][x+g] = 1
                                   

                                if tam_navio[mousepressed_up[1]][0] == 40:
                                    voce[i+g][x] = 1


        if not posicionou:                           
            for e in range(len(listanavio)):
                angulo = random.randint(0,1)
                if angulo == 0:
                    i = random.randint(0,9-tam_navio[e][2])
                    x = random.randint(0,6)
                    for k in range(tam_navio[e][2]):
                        oponente[i+k][x] = 1

                elif angulo == 1:
                    i = random.randint(0,9)
                    x = random.randint(0,6-tam_navio[e][2])
                    for k in range(tam_navio[e][2]):
                        oponente[i][x+k] = 1
                posicionou = True









        
        if clicoucomecar:
            if xx > 230 and xx < 427 and yy > 369 and yy < 419:
                
                if contador >= 2000:
                    if len(travarlista) != len(listanavio):
                        contador = 0
                    if listacomecar == 0:
                        contador = 0
                    
                while contador < 2000:
                    if len(travarlista) == len(listanavio):
                        janela.blit(comecou_image, (390,50))
                        contador += 1
                        pygame.display.update()
                        listacomecar = 1
                        comecou = 1
                        resultado = 1
                    else:
                        janela.blit(aviso_travar, (400,30))
                        contador += 1
                        pygame.display.update()
        

                

                    
            if clicoubotao and turno % 2 == 0 and comecou:
                if len(travarlista) == len(listanavio):
                        for i in range(10):
                            for x in range(7):
                                if xx > coord[0]+(i)*quadrado[0] and yy > coord[1] + (x)*quadrado[1]  and xx < coord[0]+(i+1)*quadrado[0] and yy < coord[1] + (x+1)*quadrado[1] and xis[i][x] == 0:
                                    xis[i][x] = 1
                                    xis_lista.append(1)
                                    turno += 1
            


            #turno adversario                        
            if turno % 2 != 0:
                if voce[random_i][random_x] and contador_rot < 4:
                    
                    if contador_rot == 0:
                        if random_x+1 < 6 and not xis2[random_i][random_x+1]:
                            xis2[random_i][random_x+1] = 1
                            turno += 1
                        contador_rot += 1
                    elif contador_rot == 1:
                        if random_x-1 > 0 and not xis2[random_i][random_x-1]:
                            xis2[random_i][random_x-1] = 1
                            turno += 1
                        contador_rot += 1
                    elif contador_rot == 2:
                        if random_i+1 < 9 and not xis2[random_i+1][random_x]:
                            xis2[random_i+1][random_x] = 1
                            turno += 1
                        contador_rot += 1
                    elif contador_rot == 3: 
                        if random_i-1 > 0 and not xis2[random_i-1][random_x]:
                            xis2[random_i-1][random_x] = 1
                            turno += 1   
                        contador_rot += 1

                else:
                    random_i=random.randint(0,9)
                    random_x=random.randint(0,6)
                    if contador_rot == 4:
                        contador_rot = 0
                
                    while xis2[random_i][random_x]: 
                        random_i=random.randint(0,9)
                        random_x=random.randint(0,6)
                    xis2[random_i][random_x] = 1
                    turno += 1

            








        for i in range(10):
            for x in range(7):
                if xis2[i][x]:
                    janela.blit(xis_image, (coord1[0]+(i)*quadrado[0], coord1[1] + (x)*quadrado[1]))
                if xis2[i][x] and voce[i][x]:
                    janela.blit(xis_image_verde, (coord1[0]+(i)*quadrado[0], coord1[1] + (x)*quadrado[1]))
                        
                
            
                if xis[i][x] == 1:
                    xis_lista.append(xis[i][x])
            
                if oponente[i][x] == 1:
                    oponente_lista.append(xis[i][x])
       


       #voce ganhou
        if resultado:
            perdeu = False
            for i in range(10):
                for x in range(7):
                    if oponente[i][x] - xis[i][x] > 0:
                        perdeu = True

            if not perdeu:
                janela.blit(voce_ganhou,(330,11))
                janela.blit(tentar_novamente,(342,260))
                janela.blit(sair,(572,260))
                comecou = False
                pygame.display.update()


        

        #voce perdeu
        if resultado:
            perdeu = True
            for i in range(9):
                for x in range(7):
                    if voce[i][x] - xis2[i][x] > 0:
                        perdeu = False

            if perdeu:
                janela.blit(voce_perdeu,(330,11))
                janela.blit(tentar_novamente,(342,260))
                janela.blit(sair,(572,260))
                comecou = False
                pygame.display.update()
        




                    
        clicoubotao = False
        clicoucomecar = False
        clicoutravar = False
        clicounovamente = False
        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
                                                
                    
        
        pygame.display.update()
Game()