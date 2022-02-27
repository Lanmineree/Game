import pygame
pygame.init()
import random

class Circle:
    def __init__(self,speed):
        self.x=random.randint(0,500)
        self.y=random.randint(0,500)
        self.speed = random.random()
    