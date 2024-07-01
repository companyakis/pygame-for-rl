# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:11:34 2024

@author: Mustafa Buyukdereli
"""

import pygame

pygame.init()

window = pygame.display.set_mode((900, 800))

# we can see the font types
#font_list = pygame.font.get_fonts()
#print(font_list)

font1 = pygame.font.SysFont("calibri", 60)

font2= pygame.font.SysFont("verdana", 80)

text1 = font1.render("Hi there", True, (0, 255, 0))

text1_coordinate = text1.get_rect()

text1_coordinate.topleft = (200, 250)

text2 = font2.render("PyGame for RL", False, (0, 0, 255))

text2_coordinate = text2.get_rect()

text2_coordinate.bottomright = (700, 750)

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    window.blit(text1, text1_coordinate) 
    window.blit(text2, text2_coordinate) 

    pygame.display.update()    

pygame.quit()
