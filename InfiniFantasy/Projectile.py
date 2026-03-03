#BellP7 - Supplemental
import pygame
from Sprite import AnimatedSprite
class Arrow(AnimatedSprite):
    def __init__(self, position, direction, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.speed = 5
        self.direction = direction
        self.hitbox = self.rect.inflate(-20, -20)
    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        