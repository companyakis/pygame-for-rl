# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 23:41:09 2024

@author: Mustafa Buyukdereli

Let's Create variables holding RGB colors 

Remember (Red, Green, Blue)
"""

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

import pygame

pygame.init()

x_y = (900, 800)

window = pygame.display.set_mode(x_y)

# rectangulars

pygame.draw.rect(window, RED, (0, 0, 120, 140), 15)

pygame.draw.rect(window, YELLOW, (150, 160, 340, 420))

pygame.draw.rect(window, WHITE, (500, 500, 600, 600))

state = True

while state:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            state = False
            
    pygame.display.update()
        
pygame.quit()
