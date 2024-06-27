# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 23:03:14 2024

@author: Mustafa Buyukdereli
"""

import pygame

pygame.init()

window = pygame.display.set_mode((800, 700))

super_hero = pygame.image.load("superhero.png")

super_hero_coordinates_1 = super_hero.get_rect()

super_hero_coordinates_2= super_hero.get_rect()

super_hero_coordinates_1.topleft = (15, 15)

super_hero_coordinates_2.topleft = (250, 300)

state = True

while state:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            state = False
    window.blit(super_hero, super_hero_coordinates_1)
    window.blit(super_hero, super_hero_coordinates_2)
    pygame.display.update()
    
pygame.quit()
