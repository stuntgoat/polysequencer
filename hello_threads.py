import threading
import datetime

class HelloThreads(threading.Thread):

    def run(self):
        print("%s says now is %s" % (self.getName(), datetime.datetime.now()))


def fire():
    
    for thread in xrange(10):
        HelloThreads().start()
    return None

if __name__ == "__main__":
    fire()
