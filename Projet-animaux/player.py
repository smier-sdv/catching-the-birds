import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        # On charge l'image du joueur
        self.image = pygame.image.load("assets/player.png")
        
        # redimensionner l'image
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH,PLAYER_HEIGHT))
        
        # On charge la hitbox du joueur
        self.rect = self.image.get_rect()
        
        # Positionner le joueur
        self.rect.x = SCREEN_WIDTH/2 - PLAYER_WIDTH/2
        self.rect.y = 500
        
    def move_right(self):
        if self.rect.x + PLAYER_WIDTH < SCREEN_WIDTH :
            self.rect.x += PLAYER_SPEED
    
    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED