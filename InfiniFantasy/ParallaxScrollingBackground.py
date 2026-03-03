#bellP7.py supplemental file, enables parallax scrolling background for simulated DOF effect
import pygame
class ParallaxScrollingBackground:
    def __init__(self, layerPath, windowSize):
        #layerPath = (pathToImage, parallaxSpeed)
        #windowSize = (width,height)
        #(width,height) = screen.get_size() Use this when instantiating
        
        self.layers = []
        self.windowSize = windowSize
        for path, speed in layerPath:
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image,(self.windowSize[0], self.windowSize[1]))
            self.layers.append({
                'image': image,
                'speed': speed,
                'offsetX': 0 #initial x-offset, will increase later
            })
    def update(self, deltaX):
        #deltaX is the change in player position along the x axis.
        #This will update the offset (set in __init__) for each layer based on its 'speed'
        for layer in self.layers:
            layer['offsetX'] += deltaX * layer['speed']
            
    def draw(self,surface):
        #Draw All layers
        for layer in self.layers:
            x = layer['offsetX'] % self.windowSize[0]
            surface.blit(layer['image'], (-x, 0))
            #Draw a second copy for seamless scrolling
            surface.blit(layer['image'], (self.windowSize[0]- x, 0))
                