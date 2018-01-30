#!/usr/bin/python
## Curs 3, Tema 4
## Demonstratie sys, os, re, random
## Nicolae Erast - 10.05.2017

import sys, os
import re
import time
import random

class chkpy():
    def __init__(self, ver = '2.7.13'):
        self.pkgs = []
        self.ver = ver
        self.findpy = re.compile('python\s*' + re.escape(self.ver),re.I)
        self.pause = random.randrange(80000,90000,1)

        if sys.platform == 'win32':
            self.pkgs = os.popen('wmic product get Namme,Version').readlines()
            if len(self.pkgs) > 0:
                self.alert = 'msg %USERNAME% '
                print('Checking programs with "wmic"')

        if sys.platform in ['posix','linux2']:
            self.alert = 'echo '
            self.pkgs = os.popen('rpm -qa').readlines()
            if len(self.pkgs) > 0:
                print('Checking packages with "rpm -qa"')
                return
            
            self.pkgs = os.popen('dpkg -l').readlines()
            if len(self.pkgs) > 0:
                print('Checking packages with "dpkg -l"')
                return
            
        if len(self.pkgs) == 0:
            print('Can\'t interogate installed apps')
            sys.exit(1)

    def msg(self):
        msg = msg_notfound = self.alert + ' "Please install Python '+ self.ver +'"'
        msg_found = self.alert + ' "Congratulation! You have Python ' + self.ver + '"'
        
        for pkg in self.pkgs:
            found = re.search(self.findpy, pkg)
            if found:
                msg = msg_found
                print pkg
                break
        with os.popen(msg) as o:
            print(o.read())
        sys.exit(0)

    def wait(self):
        print('Waiting: ' + str(self.pause) + ' seconds')
##        time.sleep(self.pause)

def main():
    print '''
Checking if specific python version is installed
with sys, os, re, random
    '''
    
    py = chkpy('2.7.12')
    py.wait()
    py.msg()
    
    raw_input(os.linesep + 'Press any key to exit')
    sys.exit(0)

if __name__ == '__main__':
    main()
