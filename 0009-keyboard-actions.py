# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:30:19 2024

@author: Mustafa Buyukdereli
"""

import pygame

pygame.init()

window = pygame.display.set_mode((900, 900))

velocity = 30

hero = pygame.image.load("superhero.png")

hero_coordinates = hero.get_rect()

hero_coordinates.bottomleft = (400, 450)

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero_coordinates.y -= velocity
            elif event.key == pygame.K_DOWN:
                hero_coordinates.y += velocity
            elif event.key == pygame.K_RIGHT:
                hero_coordinates.x += velocity
            elif event.key == pygame.K_LEFT:
                hero_coordinates.x -= velocity
            
    window.fill((0, 0, 0)) # black
    
    window.blit(hero, hero_coordinates)
    
    pygame.display.update()

pygame.quit()
