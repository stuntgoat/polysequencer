from time import sleep
from threading import Thread

class Mark(Thread):
    def __init__(self, pulse, quantity):
        Thread.__init__(self)
        self.pulse = pulse
        self.quantity = quantity
#        self.pulse_three = pulse_three

        
    def play(self, interval):
        for action in xrange(self.quantity):        
            print("%s" % (interval * "*"))
            print('') 
            sleep(60/interval)
        return None
        
    
    def run(self):
        self.play(self.pulse)
        
        return None

def begin(bpm_list, quantity):
    for interval in bpm_list:
        tick = Mark(interval, quantity)
        tick.start()
    
if __name__ == "__main__":
    


    for interval in [60, 30]:
        tick = Mark(interval)
        tick.start()


