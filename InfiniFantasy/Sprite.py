#bellp7 - Supplemental
import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position, characterType, frameDelay=50):
        super().__init__()
        self.characterType = characterType
        self.animations = {}
        self.frameDelays = {}
        self.state = 'idle'
        self.currentFrame = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.flipped = False
        self.loadAnimations()
        self.frames = self.animations[self.state]
        self.image = pygame.transform.flip(self.frames[self.currentFrame], self.flipped, False)
        self.frameDelay = frameDelay
        self.rect = self.image.get_rect(topleft=position)
        # Physics
        self.velocityY = 0
        self.isJumping = False
        self.gravity = 1
        self.jumpStrength = -10
        
        self.hitbox = self.rect.inflate(-20, -20)
        # Character Attributes:
        self.healthPoints = 100
        
        
        self.currentTick = pygame.time.get_ticks()

    def loadAnimations(self):
        self.basePath = f"InfiniFantasy/Assets/Characters/{self.characterType.capitalize()}/{self.characterType.capitalize()} with shadows/{self.characterType.capitalize()}-"
        self.animationFiles = {
            'idle': (f"{self.basePath}Idle.png", 100, 100, 50),
            'walk': (f"{self.basePath}Walk.png", 100, 100, 50),
            'attack': (f"{self.basePath}Attack.png", 100, 100, 50),
            'death': (f"{self.basePath}Death.png", 100, 100, 50),
            'hurt': (f"{self.basePath}Hurt.png", 100, 100, 50)
        }
        for state, (imagePath, frameWidth, frameHeight, frameDelay) in self.animationFiles.items():
            spriteSheet = pygame.image.load(imagePath).convert_alpha()
            frames = []
            sheetWidth, sheetHeight = spriteSheet.get_size()
            for y in range(0, sheetHeight, frameHeight):
                for x in range(0, sheetWidth, frameWidth):
                    frame = spriteSheet.subsurface(pygame.Rect(x, y, frameWidth, frameHeight))
                    frames.append(frame)
            self.animations[state] = frames
            self.frameDelays[state] = frameDelay

    def set_animation_state(self, newState):
        if newState in self.animations and newState != self.state:
            self.state = newState
            self.frames = self.animations[self.state]
            self.currentFrame = 0
            self.lastUpdate = pygame.time.get_ticks()

    def frameUpdate(self):
        now = pygame.time.get_ticks()
        frameDelay = self.frameDelays.get(self.state, 100)
        if now - self.lastUpdate > self.frameDelay:
            self.currentFrame = (self.currentFrame + 1) % len(self.frames)
            self.lastUpdate = now
        frame = self.frames[self.currentFrame]
        self.image = pygame.transform.flip(frame, self.flipped, False)
        self.hitbox = self.rect.inflate(-20,-20)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def hasGravity(self):
        self.velocityY += self.gravity
        self.rect.y += self.velocityY
        if self.rect.bottom >= 598:
            self.rect.bottom = 598
            self.recentlyJumped = True
            self.velocityY = 0
            self.isJumping = False
        else:
            self.recentlyJumped = False