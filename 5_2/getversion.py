#!/usr/bin/python
# Using telnet library to get software version from public router
# 28.05.2017, Nicolae Erast

host = 'route-views.routeviews.org'
user = 'rviews'
debug_lvl = 0
pattern = 'Version 15\.\d+(\(\d+\))?'

import os,re

#conectare si setare debug level
from telnetlib import Telnet
tn = Telnet()
tn.set_debuglevel(debug_lvl)
tn.open(host)

#autentificare
tn.read_until('Username: ')
tn.write(user + os.linesep)
tn.read_until('route-views>')

#command
tn.write('show version' + os.linesep)
recv = tn.read_until(' --More-- ')
found = re.search(pattern,recv)

#exit
tn.close()
tn.read_all()

#version
if found:
    print found.group(0)
else:
    print 'Didn\'t find the version'
