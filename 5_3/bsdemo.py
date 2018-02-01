#!/usr/bin/python
# Fun with beautifulsoup
# 01.06.2017, Nicolae Erast

from bs4 import BeautifulSoup as BS

import requests
page = requests.get('http://www.pmb.ro/contact/pmb/pmb_telefoane.php')
content = page.content

pb = [] #phonebook
s = BS(content, 'lxml')
table = s.find('table',{'class': 'tabel'})

for rand in table.find_all('tr'):
    rand_values = []
    for camp in rand.find_all('td'):
        value = camp.get_text('; ', strip = True)
        rand_values.append(value)
    pb.append(rand_values)

for row in pb:
    if len(row) == 1 and len(row[0]) != 0:
        print row[0]
    elif len(row) != 1:
        print row[0].ljust(100),'\t',row[1].ljust(8),'\t',row[2]
