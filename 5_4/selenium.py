#!/usr/bin/python
# Fun with selenium
# Extracting names and phone numbers from web
# This script was developed to use 'http://www.pmb.ro/contact/pmb/pmb_telefoane.php'
# Please add your own page to scan and adapt the script, if necesary
# 02.06.2017, Nicolae Erast

from selenium import webdriver
import os, time

page = 'http://www.domain.ro/contact.php'

drvpath = '/usr/lib/chromium-browser/chromedriver'
browser = webdriver.Chrome(drvpath)
browser.get(page)

print 'Waiting 3 seconds for page to load'
time.sleep(3)
print 'Scrapping...'

pb = []
rows = browser.find_elements_by_xpath('//*[@id="continut"]/table/tbody/tr')
for row in rows:
    row_values = []
    for field in row.find_elements_by_tag_name('td'):
        value = field.text.replace(os.linesep,'; ').strip()
        row_values.append(value)
    pb.append(row_values)

browser.quit()

for row in pb:
    if len(row) == 1 and len(row[0]) != 0:
        print row[0]
    elif len(row) != 1:
        print row[0].ljust(100),'\t',row[1].ljust(8),'\t',row[2]
