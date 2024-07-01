# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:45:12 2024

@author: Mustafa Buyukdereli
"""

import pygame

pygame.init()

window = pygame.display.set_mode((900, 800))

voice_start = pygame.mixer.Sound("voice/start.wav")

voice_end = pygame.mixer.Sound("voice/end.wav")

voice_start.play()

pygame.time.delay(3000)

voice_end.play()

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    pygame.display.update()    

pygame.quit()
