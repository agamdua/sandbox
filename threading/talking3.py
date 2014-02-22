'''
Three rabbits A, B and C feel adventurous and go exploring the
'threading' module. They have lofty dreams of rescuing their friend GIL.

This is how they communicate.
'''

from Queue import Queue
import threading

class Rabbit(threading.Thread):
    '''
    Class for communicating Rabbit threads
    '''

    def __init__(self, message, name):
        '''
        Constructor for rabbit object.

        Thread params:
            message: Stores the message which the thread is operating on
            name: Name of the thread for humans to identify
        '''
        threading.Thread.__init__(self)
        self.message = message
        self.name = name # is this the same as thread.name?

    def run(self): # Is this better as a separate target function?
        '''
        Adds message to queue if empty, else retrieves the message
        and adds one to it, adding the new value to queue
        '''
        # while True:
        item = msg_q.get()
        if item is None:
            msg_q.put(100)
            msg_q.get() # Get value off FIFO queue, not necessarily 100

        # Process item
        item = item + 1
        print item

        # Add item to queue and mark task as done
        msg_q.put(item)
        msg_q.task_done()
        return

rabbit_info = { "Al": None,
                "Bo": 500,
                "Calvin": 720,
              }

msg_q = Queue()

for k,v in rabbit_info.items():
    print k
    t = Rabbit(name=k, message=v).start()
