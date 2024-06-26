# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:31:28 2024

@author: Mustafa Büyükdereli
"""

import pygame

pygame.init()

x_y = (600, 400)

window = pygame.display.set_mode(x_y)

state = True

while state:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            state = False
            
pygame.quit()
