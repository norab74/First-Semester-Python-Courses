#BellP7 - Supplemental
import pygame
import random
class Rain(pygame.sprite.Sprite):
    def __init__(self):
        self.weather_sheet = pygame.image.load("InfiniFantasy/Assets/Foreground/rain effect.png").convert_alpha()
        self.rain_frames = []
    def createWeatherSheet(self):
        for i in range(6):
            frame = self.weather_sheet.subsurface(pygame.Rect(i * 50, 0, 50, 50))
            self.rain_frames.append(frame)
    def draw_rain(self, surface, rain_frames, count=30):
        for _ in range(count):
            try:
                frame = random.choice(rain_frames)
            except IndexError:
                pass
            x = random.randint(0, surface.get_width()-50)
            y = random.randint(0, surface.get_height()-50)
            surface.blit(frame, (x, y))
    