import pygame

import sys

pygame.init()

window = pygame.display.set_mode((1000, 900))

pygame.display.set_caption("Target shooting game by Mustafa Buyukdereli")

window_icon = pygame.image.load("./pictures/iconshoot.png")

pygame.display.set_icon(window_icon)

clock = pygame.time.Clock()

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
            sys.exit()
            
    pygame.display.update()
    
pygame.quit()
