#!/usr/bin/python
# Curs 2, Tema 2
# Tema 1, modificata pentru tema 2
# Nicolae Erast - 02.05.2017

import os

__all__ = ['Test']

class X(type):
    def __init__(self, cls, base, attr):
        for klass in base:
            if isinstance(klass, X):
                raise TypeError('forbidden inheritance')


class txt_desc(object):
    def __init__(self):
        self.attr = []

    def __get__(self, obj, cls):
        print self.attr

    def __set__(self, obj, val):
        self.attr.append(val)

    def __delete__(self, obj):
        print 'attribute can\'t be deleted'
        

class Test(object):
    __metaclass__ = X

    nume = txt_desc()
    prenume = txt_desc()
    clasa = txt_desc()
    
    def __init__(self, csv):
        f = open(csv,'r')
        line = f.readline()
        for line in f:
            n, p, c = line.strip().split(',')
            self.nume = n
            self.prenume = p
            self.clasa = c
        f.close

def main():
    print '''
Demo using package and "os" module
    '''
    
    print '\nInitializez obiect "o" cu parametrul "mycvs.csv"'
    try:
        o = Test('mycvs.csv')
    except IOError:
        print 'file not found... looking in root folder'
        os.chdir('..')
        o = Test('mycvs.csv')
        if o:
            print 'found in', os.getcwd()
    finally:
        print 'Initialized'
        
    print '\nPrint "o.nume", "o.prenume", "o.clasa"'
    o.nume
    o.prenume
    o.clasa

    print '\nTrying "del o.clasa"'
    del o.clasa

    print '\nTrying inheritance of "readcsv":'
    print 'class ImportInterzis(Test):'
    print '\tpass'
    
    raw_input('\nPress any key for output')
    class ImportInterzis(Test):
        pass

if __name__ == '__main__':
    main()
