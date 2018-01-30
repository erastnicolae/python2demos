#!/usr/bin/python
# Nicolae Erast, 03.06.2017

from __future__ import print_function
from multiprocessing import Pool
import sys, os

if os.name == 'posix':
    ping_cmd = 'ping -c 2 8.8.8.8'
elif os.name == 'nt':
    ping_cmd = 'ping -n 2 8.8.8.8'
else:
    print('Platform not supported')
    sys.exit(1)

def gping(i):
    r = os.popen(ping_cmd)
    for line in r:
        if line.strip():
            print('Process ' + str(i) + ': ' + line, end = '')

def main():
    p = Pool()
    p.map(gping, range(11))
    p.close()
    p.join()

    raw_input(os.linesep + 'Press any key to exit ... ')
if __name__ == '__main__':
    main()
