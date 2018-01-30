#!/usr/bin/python
# 17.05.2017, Nicolae Erast

import sys
import re
import os.path
import csv
from collections import OrderedDict
import json


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

    # formating data
    data_list = list()
    for row in data[1:]:
        data_dict = OrderedDict()
        for i, header in enumerate(data[0]):
            data_dict[header] = row[i]
        data_list.append(data_dict)

    data_dict = {'Car owners': data_list}
    print json.dumps(data_dict)

    # writing json
    with open(fname + '.json','w') as fjson:
        json.dump(data_dict,fjson)
        print('Conversion csv->json done!')

    raw_input(os.linesep + 'Press any key to exit')
    sys.exit(0)

if __name__ == '__main__':
    main()
