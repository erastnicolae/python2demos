#!/usr/bin/python
# 15.05.2017, Nicolae Erast

import sys
import re
import os.path
import csv
import sqlite3

def main():
    
    # if i run the script from idle passing the file
    if 'idlelib.run' in sys.modules:
        sys.argv.append('mycsv')
    
    # checking for csv file
    fcsv = sys.argv[1:]
    if len(fcsv) != 1:
        print('Please give me the file name! Exiting ...')
        sys.exit(1)
    fcsv = fcsv[0]
    
    # checking if provided file have .csv extension
    fext = re.search('\.csv$', fcsv, re.I)
    if not fext:
        fcsv += '.csv'
    fname = fcsv.replace('.csv','')

    # checking if file exists
    if not os.path.isfile(fcsv):
        print('No file with that name. Exiting ...')
        sys.exit(1)

    # reading the file
    with open(fcsv, 'r') as f:
        data = csv.reader(f, delimiter=',',quoting=False) 
        data = list(data)

    # checking number of columns
    if len(data[0]) != 3:
        print('File incompatible with the defined database')
        sys.exit(1)

    # inserting and printing
    with sqlite3.connect('sqlite.db') as db:
        
        # emptying the database
        sql = 'DELETE FROM import; VACUUM;'
        db.executescript(sql)

        # inserting data
        sql = 'INSERT OR REPLACE INTO'
        sql += ' import(nume, prenume, clasa)'
        sql += ' VALUES(?, ?, ?)'
        db.executemany(sql, data[1:])

        # extracting and printing
        sql = 'SELECT * FROM import'
        for row in db.execute(sql):
            print '\t'.join(row)

    raw_input(os.linesep + 'Press any key to exit')
    sys.exit(0)
    
if __name__ == '__main__':
    main()
