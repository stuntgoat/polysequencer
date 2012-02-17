"""Install gstreamer, gst-python(needed pykg-config, in place of missing pkg-config)"""
from os import fork
from pygame import mixer as m
from time import sleep
from threading import Thread


sound_list = []
m.init()
sound_list.extend([m.Sound('hey.ogg'), m.Sound('hi.ogg'), m.Sound('ho.ogg')])

channel_list = []
for i in xrange(8):
    channel_list.append(m.Channel(i))

def play_sounds_with_fork():
    for channel in channel_list:
        pid = fork()
        print pid
        channel.play(sound_list[channel_list.index(channel)%3])
        sleep(.2)
        
if __name__ == "__main__":
    play_sounds_with_fork()
    # play_sounds()
    sleep(4)


    



# class ThreadedSoundPlayer(Thread):
#     def __init__(self, channel, sound):
#         super(ThreadedSoundPlayer, self).__init__()
#         self.channel = channel
#         self.sound = sound
#     def run(self):
#         pid = fork()
#         if pid != 0:
#             self.channel.play(self.sound)
        
# def play_sounds():
#     for channel in channel_list:
#         tsp = ThreadedSoundPlayer(channel, sound_list[channel_list.index(channel)%3])
#         tsp.start()
