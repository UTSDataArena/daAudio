from daAudio.engine.openal.audio import SoundSource


class AudioEmitter(object):

    def __init__(self, name):
        super(AudioEmitter, self).__init__()
        
        self.name = name
        self.source = SoundSource()

    def set_position(self, position):
        self.source.position = position

    def set_looping(self, looping):
        self.source.looping = looping

    def queue(self, audio):
        self.source.queue(audio)
