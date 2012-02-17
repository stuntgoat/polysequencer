"""Install gstreamer, gst-python(needed pykg-config, in place of missing pkg-config)"""

from pygame import mixer as m
from time import sleep
from threading import Thread


sound_list = []
m.init()
sound_list.append(m.Sound('hey.ogg'))
sound_list.append(m.Sound('hi.ogg'))
sound_list.append(m.Sound('ho.ogg'))


class ThreadedSoundPlayer(Thread):
    def __init__(self, channel, sound):
        super(ThreadedSoundPlayer, self).__init__()
        self.channel = channel
        self.sound = sound
    def run(self):
        self.channel.play(self.sound)
        sleep(2)

channel_list = []
for i in xrange(8):
    channel_list.append(m.Channel(i))
    
def play_sounds():
    for channel in channel_list:
        tsp = ThreadedSoundPlayer(channel, sound_list[channel_list.index(channel)%3])
        tsp.start()

if __name__ == "__main__":

    play_sounds()
    sleep(4)


    


