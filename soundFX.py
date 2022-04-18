import pygame

class SoundFX():
    def __init__(self):
        self.sounds = {}

        self.sounds["bullet"] = pygame.mixer.Sound("Assets/SoundFx/antimaterhit.wav")
        self.sounds["explosion1"] = pygame.mixer.Sound("Assets/SoundFx/explosion1.wav")
        self.sounds["explosion4"] = pygame.mixer.Sound("Assets/SoundFx/explosion4.wav")
        self.sounds["laser6"] = pygame.mixer.Sound("Assets/Digital_SFX_Set/laser6.ogg")
        self.sounds["shield2"] = pygame.mixer.Sound("Assets/SoundFx/Shields/spaceshieldsounds2.ogg")
        self.sounds["shield4"] = pygame.mixer.Sound("Assets/SoundFx/Shields/spaceshieldsounds4.ogg")
        self.sounds["thrust"] = pygame.mixer.Sound("Assets/SoundFx/THRUST.WAV")

    def playSound(self,soundName, maxTime=0):
        channel = self.sounds[soundName].play(0,maxTime,0)

    def playSoundContinuously(self,soundName):
        channel = self.sounds[soundName].play(-1)

    def stopSound(self,soundName):
        channel = self.sounds[soundName].stop()

