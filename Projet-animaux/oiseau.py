import pygame
import random
from constants import *

class Oiseau(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/oiseau.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(100, SCREEN_WIDTH-100)
        self.rect.y = 0
        
        
    def tomber(self):
        if self.rect.y < SCREEN_HEIGHT:
            self.rect.y += BIRD_SPEED