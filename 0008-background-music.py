# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:57:12 2024

@author: Mustafa Buyukdereli
"""

import pygame

pygame.init()

window = pygame.display.set_mode((900, 800))

pygame.mixer.music.load("voice/horror.mp3") # background song

pygame.mixer.music.play(-1, 0.0) # continue and starting point

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    pygame.display.update()    

pygame.quit()
