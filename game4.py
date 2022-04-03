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
    def update(self,t,mouse_pos):
        self.time += t
        score=''
        if self.time>1000:
            self.__init__(self.screen)
            score='-0.5'
        elif self.is_click(mouse_pos):
            score= '+1'
            #k
        elif not self.is_click(mouse_pos):
            score= '-1'
        else:
            self.radius+=0.5
        pygame.draw.circle(self.screen,(self.r,self.g,self.b),(self.x,self.y),self.radius)
    def is_click(self,mouse_pos):
        #This function will get the mouse position
        #Check if the circle was clicked or not
        #Return true when the circle was clicked and false when it was not clicked
        #radius
        #center
        #mouse_pos
        #find x and y coordinates
        x= self.x-mouse_pos[0]
        y= self.y-mouse_pos[1] 
        #หาเส้นทะแยง
        diagonal_two=x*x+y*y
        diagonal=diagonal_two**1/2
        #เปรียบเทียบกับ r ว่าเยอะหรือน้อยกว่า
        if diagonal <= self.radius:
            return True
        else:
            return False
running = True

list = []
for i in range(1):
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
    mouse_pos=pygame.mouse.get_pos()
    for a in list:
        a.update(time,mouse_pos)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
