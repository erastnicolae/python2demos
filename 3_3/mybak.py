#!/usr/bin/python
## Nicolae Erast - 10.05.2017

import os, sys, re, time, tarfile

class myarch():

    def __init__(self):
        self.path = os.getcwd()
        print('Current path: "%s"' % self.path)

        self.name = time.strftime('%Y_%m_%d_%I_%S_bak.tar.gz')

        self.files = []
        for f in os.listdir(self.path):
            if re.search('\.py$',f,re.I):
                self.files.append(f)
                
    def archive(self):
        with tarfile.open(self.name,'w:gz') as archfile:
            print(os.linesep + 'Archiving...')
            for f in self.files:
                print(' - ' + f)
                archfile.add(f)
            print(os.linesep + 'Archive ' + self.name + ' finished') 

def main():
    print '''
Backup with sys, os, re, time, tarfile
    '''

    arch = myarch()
    arch.archive()
    
    raw_input(os.linesep + 'Press any key to exit')
    sys.exit(0)

if __name__ == '__main__':
    main()
