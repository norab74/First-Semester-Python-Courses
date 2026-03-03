#BellP7 - Supplemental
import pygame
class SoundEngine: #this was gonna be bigger, it doesn't need to be


    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_volume = .5
        self.sfx_volume = 0.7
        #attempt to load Sounds
    def loadSound(self, name, path):
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(self.sfx_volume)
            self.sounds[name] = sound
        except pygame.error as e:
            print(f"Error locating sound file: {e}")
    
        #Attempt to play them
    def playSound(self,name):
        if name in self.sounds:
            self.sounds[name].play()
            print(f"Playing sound: {name}")
        else: print(f"Sound File: {name} not found")
    
        #Loop BGM
    def loopBackgroundMusic(self, path, loops=-1):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(loops)
            print(f"Playing music")
        except pygame.error as e:
            print(f"Error Playing music File: {e}")
