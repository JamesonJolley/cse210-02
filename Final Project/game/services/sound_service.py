from playsound import playsound
import time


class Sound_service:
    def __init__(self):
        self.sounds={}
        self.prepare_sounds() 
        self.time_started=0
        
    def add_sound(self,key,sound,Sound_duration=0):
        """
        adds a sound to the sounds dict 

         Args:
            sound (sound): the path of the sound file
            key (key): the key of the sound in the dict
            Sound_duration (Sound_duration): the duration of the sound in negative fractional seconds (Optional: only required for the play continuous method)
        """
        self.sounds[key] = [sound,Sound_duration]

    def get_sound(self,key):
        """
        gets a sound to the sounds dict 

         Args:
           key (key): the key of the sound in the dict
        """
        return self.sounds[key]

    def set_sound(self,key,Sound_duration=0):
        """
        updates a sound in the sounds dict 

         Args:
            sound (sound): the path of the sound file
            key (key): the key of the sound in the dict
            Sound_duration (Sound_duration): the duration of the sound in negative fractional seconds (Optional: only required for the play continuous method)
        """
        self.sounds[key] = [sound,Sound_duration]

    def play_sound(self,key):
        """
        playes a sound in the sounds dict 

         Args:
            key (key): the key of the sound in the dict
        """
        playsound(self.sounds[key][0])

    def prepare_sounds(self):
        """
        prepares the sounds dict 
        """
        self.add_sound('open','game/Assets/mixkit-video-game-retro-click-237.wav')
        self.add_sound('song', 'game/Assets/Tetris.mp3',-1.301739848)

    def play_continuous(self,key='song'):
        sound = self.get_sound(key)
        time_dif = self.time_started - time.process_time()
        print(time_dif)
        print(sound[1])
        if time_dif == 0:
            self.time_started=time.process_time()
            playsound(sound[0])
        if time_dif <= sound[1]:
            self.time_started=time.process_time()
            playsound(sound[0])
        else:
            pass

        
        