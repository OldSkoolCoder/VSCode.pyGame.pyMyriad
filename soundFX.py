import pygame

class SoundFX():
    def __init__(self):
        self.sounds = {}

        self.sounds["bullet"] = pygame.mixer.Sound("Assets/SoundFx/antimaterhit.ogg")
        pygame.mixer.Sound.set_volume(self.sounds['bullet'],.25)
        self.sounds["explosion1"] = pygame.mixer.Sound("Assets/SoundFx/explosion1.ogg")
        pygame.mixer.Sound.set_volume(self.sounds['explosion1'],.25)
        self.sounds["explosion4"] = pygame.mixer.Sound("Assets/SoundFx/explosion4.ogg")
        pygame.mixer.Sound.set_volume(self.sounds['explosion4'],.25)
        self.sounds["laser6"] = pygame.mixer.Sound("Assets/SoundFx/laser6.ogg")
        #pygame.mixer.Sound.set_volume(self.sounds['laser6'],.25)
        self.sounds["laser3"] = pygame.mixer.Sound("Assets/SoundFx/laser3.ogg")
        #pygame.mixer.Sound.set_volume(self.sounds['laser3'],.25)
        self.sounds["laser9"] = pygame.mixer.Sound("Assets/SoundFx/laser9.ogg")
        #pygame.mixer.Sound.set_volume(self.sounds['laser9'],.25)
        self.sounds["shield2"] = pygame.mixer.Sound("Assets/SoundFx/Shields/spaceshieldsounds2.ogg")
        self.sounds["shield4"] = pygame.mixer.Sound("Assets/SoundFx/Shields/spaceshieldsounds4.ogg")
        self.sounds["thrust"] = pygame.mixer.Sound("Assets/SoundFx/THRUST.WAV")
        pygame.mixer.Sound.set_volume(self.sounds['thrust'],.25)
        self.sounds["round1"] = pygame.mixer.Sound("Assets/VoiceOver/round1.ogg")
        self.sounds["round2"] = pygame.mixer.Sound("Assets/VoiceOver/round2.ogg")
        self.sounds["round3"] = pygame.mixer.Sound("Assets/VoiceOver/round3.ogg")
        self.sounds["round4"] = pygame.mixer.Sound("Assets/VoiceOver/round4.ogg")
        self.sounds["round5"] = pygame.mixer.Sound("Assets/VoiceOver/round5.ogg")
        self.sounds["round6"] = pygame.mixer.Sound("Assets/VoiceOver/round6.ogg")
        self.sounds["round7"] = pygame.mixer.Sound("Assets/VoiceOver/round7.ogg")
        self.sounds["round8"] = pygame.mixer.Sound("Assets/VoiceOver/round8.ogg")
        self.sounds["round9"] = pygame.mixer.Sound("Assets/VoiceOver/round9.ogg")
        self.sounds["readySetGo"] = pygame.mixer.Sound("Assets/VoiceOver/ReadySetGo.ogg")

        self.gameMusic = pygame.mixer.music.load("Assets/GameMusic/GameMusic1.ogg")
        pygame.mixer.music.set_volume(.25)

    def playSound(self,soundName, maxTime=0):
        channel = self.sounds[soundName].play(0,maxTime,0)

    def playSoundContinuously(self,soundName):
        channel = self.sounds[soundName].play(-1)

    def stopSound(self,soundName):
        channel = self.sounds[soundName].stop()

