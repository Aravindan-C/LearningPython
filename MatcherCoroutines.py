__author__ = 'aravindan'
# A set of matcher coroutines

matchers= [ print_matches("python"),print_matches("guido"),print_matches("jython")]

#prep all of the matchers by calling next()
for m in matchers:m.next()

#feed an active log file into all matchers.note for this to work,a web server must be actively writing data to the log.

wwwlog =tail(open("access-log"))
for line in wwwlog:
    for m in matchers:
        m.send(line)          # send data into each matcher coroutine