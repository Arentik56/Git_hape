import pygame, sys

pygame.init() 
clock = pygame.time.Clock()

screen_width = 900
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("sprites/background.png")
pygame.mouse.set_visible(False)

update_time = 30

while(True): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.guit()
           sys.exite()
           
    pygame.display.flip
    screen.blit(background, (0, 0))

    clock.tick(update_time)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             