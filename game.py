import pygame
pygame.init()
import random
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
class Ball:
    def __init__(self,y,speed,radius,screen):
        self.r=random.randint(0,255)
        self.g=random.randint(0,255)
        self.b=random.randint(0,255)
        self.screen=screen
        self.x=random.randint(0,500)
        self.y = y
        self.speed = random.random()
        self.radius = radius
    def update(self):
        self.y+=self.speed
        pygame.draw.circle(self.screen, (self.r,self.g,self.b), (self.x, self.y), 10)
        if self.y >= 500:
            self.y = 0
balls=[]
for i in range(100):
    ball = Ball(random.randint(0,500),0.5,10,screen)
    balls.append(ball)

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        # Fill the background with white
    screen.fill((255, 255, 255))
    for ball in balls:
        ball.update()

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()