from playsound import playsound

class Sound_service:
    def __init__(self):
        self.sounds={}
        self.prepare_sounds() 

    def add_sound(self,key,sound):
        """
        adds a sound to the sounds dict 

         Args:
            sound (sound): the path of the sound file
            key (key): the key of the sound in the dict
        """
        self.sounds[key] = sound

    def get_sound(self,key):
        """
        gets a sound to the sounds dict 

         Args:
           key (key): the key of the sound in the dict
        """
        return self.sounds[key]

    def set_sound(self,key,sound):
        """
        updates a sound in the sounds dict 

         Args:
            sound (sound): the path of the sound file
            key (key): the key of the sound in the dict
        """
        self.sounds[key] = sound

    def play_sound(self,key):
        """
        playes a sound in the sounds dict 

         Args:
            key (key): the key of the sound in the dict
        """
        playsound(self.sounds[key])

    def prepare_sounds(self):
        """
        prepares the sounds dict 
        """
        self.add_sound('open','game/Assets/mixkit-video-game-retro-click-237.wav')