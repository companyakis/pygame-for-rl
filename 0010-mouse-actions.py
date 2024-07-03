# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:52:59 2024

@author: Mustafa Buyukdereli
"""

import pygame

pygame.init()

window = pygame.display.set_mode((900, 1000))

hero = pygame.image.load("superhero.png")
hero_coordinates = hero.get_rect()
hero_coordinates.topleft = (300, 350)

state = True

while state:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            state = False
        
        # Mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event)
            """
            <Event(1025-MouseButtonDown {'pos': (426, 700), 'button': 1, 'touch': False, 'window': None})>
            """
            mouse_x_val = event.pos[0]
            mouse_y_val = event.pos[1]
            hero_coordinates.x = mouse_x_val
            hero_coordinates.y = mouse_y_val
    
    window.fill((0, 0, 0)) ## black color => depends on game background color!       
    window.blit(hero, hero_coordinates)
    pygame.display.update()

pygame.quit()
