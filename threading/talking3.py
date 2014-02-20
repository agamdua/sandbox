'''
Three rabbits A, B and C feel adventurous and go exploring the
'threading' module. They have lofty dreams of rescuing their friend GIL.

This is how they communicate.
'''

import threading, time

class Rabbit(threading.Thread):
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message
    def run(self):
        if self.message:
            self.message = self.message + 1
            print self.message
            time.sleep(3)
            self.run()
        else:
            print "No message"
            self.message = 1
            time.sleep(1)
            self.run()
        return

r1 = Rabbit(7)
r1.start()

r2 = Rabbit(None)
r2.start()

r3 = Rabbit (500)
r3.start()
