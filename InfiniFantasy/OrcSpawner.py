#bellP7 Supplemental
import pygame
import random
from Sprite import AnimatedSprite
class OrcSpawner():
    def __init__(self, screenWidth, yPosition):
        self.screenWidth = screenWidth
        self.yPosition = yPosition
        self.spawnedOrcs = pygame.sprite.Group()
        self.nextSpawnTime =  pygame.time.get_ticks() + random.randint(4000,8000)
    def update(self, currentTick):
        if currentTick >= self.nextSpawnTime:
            numNewOrcs = random.randint(1,3)
            for _ in range(numNewOrcs):
                spawnX = self.screenWidth + random.randint(50,300)
                newOrc = AnimatedSprite(position=(spawnX, self.yPosition), characterType='orc')
                newOrc.flipped = True
                newOrc.set_animation_state('walk')
                self.spawnedOrcs.add(newOrc)
            self.nextSpawnTime = currentTick + random.randint(4000, 8000)
        #Handle various behaviors for various states of orc
        for orc in self.spawnedOrcs:
            try:
                if orc.healthPoints == 100  : orc.rect.x -= 2
                orc.frameUpdate()
            except UnboundLocalError:
                pass
            if orc.healthPoints == 50   : 
                orc.rect.x -= 0
                orc.hurtAt=currentTick
                orc.set_animation_state('hurt')
                try:
                    if currentTick - orc.hurtAt >= 500:
                        orc.rect.x -= 1
                except UnboundLocalError:
                    pass
            if orc.healthPoints == 0:
                orc.rect.x -= 0
                orc.timeOfDeath = currentTick
                orc.set_animation_state('death')
            if orc.healthPoints == 0 and currentTick - orc.timeOfDeath >= 1000:
                orc.kill()

                
                
    def draw(self,surface):
        for orc in self.spawnedOrcs:
            orc.frameUpdate()
            orc.hasGravity()
            orc.draw(surface)
            