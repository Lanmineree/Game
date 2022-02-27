import pygame
pygame.init()
import random
from pygame.time import Clock
time=0
screen = pygame.display.set_mode([500, 500])
clock=pygame.time.Clock()
class Ball:
    def __init__(self,screen):
        self.radius = 5
        self.r = random.randint(120,255)
        self.g = random.randint(120,255)
        self.b = random.randint(120,255)
        self.x = random.randint(0,500)
        self.y = random.randint(0,500)
        self.time = 0
        self.screen = screen
    def update(self,t):
        self.time += t
        if self.time>1000:
            self.__init__(self.screen)
        else:
            self.radius+=0.5
        pygame.draw.circle(self.screen,(self.r,self.g,self.b),(self.x,self.y),self.radius)
running = True

list = []
for i in range(100):
    ball=Ball(screen)
    list.append(ball)
while running:
    time=clock.tick(60)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    # for a in range(100):
    #     list[a].update(time)
    for a in list:
        a.update(time)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
