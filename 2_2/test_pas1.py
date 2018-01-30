#!/usr/bin/python
# Nicolae Erast - 02.05.2017

from test.modul import Test as myCSV

def main():
    print 'Demo importing and renaming class'


    print '\nInitializing object "o" of class myCSV'
    try:
        o = myCSV('mycsv.csv')
    except IOError:
        print 'File "mycsv.csv" missing'

    print '\nDisplay "o.nume", "o.prenume", "o.clasa"'
    o.nume
    o.prenume
    o.clasa

if __name__ == '__main__':
    main()
