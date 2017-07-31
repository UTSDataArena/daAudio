from daAudio.engine.openal.audio import SoundSource


class Emitter(object):

    def __init__(self, name):
        super(Emitter, self).__init__()
        
        self.name = name
        self.source = SoundSource()
