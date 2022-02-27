import pygame
from pygame.time import Clock
pygame.init()
import random
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
clock=pygame.time.Clock()
x=random.randint(0,500)
y=random.randint(0,500)
font = pygame.font.SysFont(None, 24)
score=0

size=5
speed=20/3
show=True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt=clock.tick(60)/1000
    screen.fill((255, 255, 255))
    img = font.render('score'+str(score), True, (0,0,100))
    screen.blit(img, (20, 20))

    if show==True:
        pygame.draw.circle(screen,(0,0,130),(x,y),size)
    if size >=25:
        size = size
        show = False
    else:
        size+=speed*dt
    print(dt)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()