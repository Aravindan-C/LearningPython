__author__ = 'aravindan'
#tail a file (like tail -f)
import time
def tail(f):
    f.seek(0,2)  #move to EOF
    while True :
        line =f.readline()     # Try reading a new line of text
        if not line:
            time .sleep(0.1)
            continue
        yield line

"""Specific substring in a sequence of lines"""

def grep(lines,searchtext) :
    for line in lines:
        if searchtext in line :yield line

# A python implementation of unix "tail -f | grep python"
wwwlog=tail(open("active-log"))
pylines=grep (wwwlog,"drac_run_id")
for line in pylines:
    print line,