class Device:
    """
    srf - signal reception frequency - частота приема сигнала
    stf - signal transmission frequency - частота передачи сигнала
    """
    def __init__(self, srf, stf, sound=True, video=False, communicate=False):
        self.srf = srf
        self.stf = stf
        self.sound = sound
        self.video = video
        self.communicate = communicate

    def __reception(self):
        pass

    def __transmission(self):
        pass

    def on_off(self):
        self.__reception()

    def change_volume(self):
        pass

    def call(self):
        if self.communicate:
            self.__transmission()



