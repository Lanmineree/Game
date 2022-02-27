import random
import pygame
import math
class MyCircle:
    def __init__(self,surface):
        self.surface = surface
        self.x=random.randint(50,450)
        self.y=random.randint(50,450)
        self.size=5
        self.max_size=20
        self.rate=5
        self.r=random.randint(0,255)
        self.g=random.randint(0,255)
        self.b=random.randint(0,255)
    def update(self,dt,mouse_x,mouse_y,is_pressed):
        is_click=self.check_clicked(mouse_x,mouse_y)
        if is_click==True and is_pressed==True:
            return '+ score'
        if self.size<self.max_size:
            self.size+=dt*self.rate
            pygame.draw.circle(self.surface,(self.r,self.g,self.b),(self.x,self.y),self.size)
            return True
        else:
            return None
    def check_clicked(self,mouse_x,mouse_y): 
        x1, y1 = mouse_x,mouse_y
        x2, y2 = self.x,self.y
        distance = math.hypot(x1 - x2, y1 - y2)
        if distance<self.size:
            return True
        else:
            return False