from daAudio.engine.openal.audio import SoundSink


class Player(object):

    def __init__(self, device=None, listener=None):
        super(Player, self).__init__()

        self.sink = SoundSink(device) 
        self.sink.activate()

        if listener:
            self.sink.set_listener(listener)

    def play(self, emitters):
        self.sink.play(self.__extract_sources(emitters))

    def stop(self, emitters):
        self.sink.stop(self.__extract_sources(emitters))

    def pause(self, emitters):
        self.sink.pause(self.__extract_sources(emitters))

    def rewind(self, emitters):
        self.sink.rewind(self.__extract_sources(emitters))

    def update(self):
        self.sink.update()

    def __extract_sources(self, emitters):
        return [emitter.source for emitter in emitters]
        
