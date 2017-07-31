from daAudio.engine.openal.audio import SoundSource


class AudioEmitter(object):

    def __init__(self, name):
        super(AudioEmitter, self).__init__()
        
        self.name = name
        self.source = SoundSource()
