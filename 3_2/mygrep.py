#!/usr/bin/python
## Nicolae Erast - 10.05.2017

import sys, re, os

class mygrep():

    def __init__(self, tipar):
        self.path = os.getcwd()
        print('Directory to search: "%s"' % self.path)

        self.tipar = re.compile(tipar)
        print(os.linesep + 'Searching for: "%s"' % self.tipar.pattern)

    def files(self):
        self.files = []
        for paths in os.walk(self.path):
            if not paths[1]:
                for f in paths[2]:
                    self.files.append(os.path.join(paths[0],f))
        print(os.linesep + 'Checked files:')
        for f in self.files:
            print (' - %s ' % f)

    def search(self):
        self.founds = []
        for f in self.files:
            with open(f,'r') as openfile:
                fetchfile = openfile.readlines()
                for linenr, line in enumerate(fetchfile,1):
                    found = re.search(self.tipar, line)
                    if found:
                        self.founds.append([f,linenr,line,found.group()])

    def __str__(self):
        self.files()
        self.search()
        founds = len(self.founds)
        if founds: 
            prev_file = None
            for found in self.founds:
                if prev_file != found[0]:
                    prev_file = found[0]
                    print(os.linesep + 'In file:\t%s' % prev_file)
                print('Line %d:\t%s\t\ti found: %s' \
                      % (found[1], found[2].strip(), found[3]))
            return os.linesep + 'Finished search ... with ' + str(founds) + ' result(s)'
        else:
            return os.linesep + 'No match found ...'


def main():
    print '''
Demo os.walk si re, win/*nix
    '''

    tipar = ''
    arg_len = len(sys.argv) 
    if arg_len > 1:
        tipar = ' '.join(sys.argv[1:arg_len])
    else:
        while len(tipar) == 0:
            tipar = raw_input('Enter pattern to search: ')
        
    mysearch = mygrep(tipar)
    print(mysearch)

    raw_input(os.linesep + 'Press any key to exit')
    sys.exit(0)

if __name__ == '__main__':
    main()
