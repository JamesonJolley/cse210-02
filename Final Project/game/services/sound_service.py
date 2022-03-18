import winsound 

class Sound_service:
    def __init__(self):
        self.sounds={}

    def add_sound(self,sound,name):
        """
        adds a sound to the sounds dict 

         Args:
            sound (sound): the path of the sound file
            name (name): the dict key the path will be under
        """
        self.sounds[name] = sound

