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

# circles

pygame.draw.circle(window, WHITE, (400, 450), 80)

pygame.draw.circle(window, YELLOW, (600, 200), 120)

state = True

while state:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            state = False
            
    pygame.display.update()
        
pygame.quit()
