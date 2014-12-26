__author__ = 'aravindan'
"""A function can also be written to operate as a task that processes a sequence of inputs send to it,this type of function is known as coroutine"""
def print_matches(matchtext) :
    print "Looking for" ,matchtext
    while True:
        line =(yield)    # get a line of text
        if matchtext in line:
            print line
matcher=print_matches("python")
matcher.next()
matcher.send("Hello World")
matcher.send ("python is cool")
matcher.send ("python is not cool")
