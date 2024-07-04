import pygame

pygame.init()

window =pygame.display.set_mode((800, 700))

velocity = 25 # FPS

clock = pygame.time.Clock()

hero = pygame.image.load("superhero.png")

hero_coordinates = hero.get_rect()

hero_coordinates.topleft = (300, 350) 

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
            
    key = pygame.key.get_pressed()
    
    if key[pygame.K_UP]:
        hero_coordinates.y -= velocity
        
    elif key[pygame.K_DOWN]:
        hero_coordinates.y += velocity
        
    elif key[pygame.K_RIGHT]:
        hero_coordinates.x += velocity
        
    elif key[pygame.K_LEFT]:
        hero_coordinates.x -= velocity  
        
    window.fill((0, 0, 0)) 
                
    window.blit(hero, hero_coordinates)
    pygame.display.update()
    
    clock.tick(velocity)

pygame.quit()
