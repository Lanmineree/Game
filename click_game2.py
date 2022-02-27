import pygame
from my_circle import MyCircle
from pygame.time import Clock
pygame.init()
pygame.font.init()
import random
# Set up the drawing window
myfont = pygame.font.SysFont('Comic Sans MS', 30)
score=0
screen = pygame.display.set_mode([500, 500])
clock=pygame.time.Clock()
a=MyCircle(screen)
speed=5
show=True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt=clock.tick(60)/1000
    screen.fill((255, 255, 255))
    x,y=pygame.mouse.get_pos()
    is_click=pygame.mouse.get_pressed()[0]
    result = a.update(dt,x,y,is_click)
    if result== '+ score':
        score+=5
        speed+=0.5
        a=MyCircle(screen)
        a.rate=speed
    if result == None:
        score-=0.5
        a=MyCircle(screen)
        a.rate=speed
    print(score)
    textsurface = myfont.render('score: '+str(score), False, (200, 0, 0))
    screen.blit(textsurface,(10,0))
    pygame.display.flip()
# Done! Time to quit.
pygame.quit()