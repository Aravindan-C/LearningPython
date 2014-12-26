__author__ = 'aravindan'

class EventHandler(object):
    @staticmethod
    def dispatcherThread():
        while(1):
            #wait for requests

EventHandler.dispatcherThread()        # call method like a function