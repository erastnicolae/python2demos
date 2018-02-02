#!/usr/bin/python
# Demo using ntplib, smtplib, getpass
# Get current time from ntp server and send it by email using yahoo account
# 28.05.2017, Nicolae Erast

from ntplib import NTPClient
from time import ctime
import smtplib
import getpass
import sys

# add bellow email address
to = 'email@domain.ro'

c = NTPClient()
r = c.request('2.ro.pool.ntp.org')
print 'Current date and time is: ', ctime(r.tx_time)

try:
    # using ssl
##    m = smtplib.SMTP_SSL()
##    m.connect('smtp.mail.yahoo.com',465)
    # cu tls
    m = smtplib.SMTP()
    m.connect('smtp.mail.yahoo.com',587)
    m.starttls()
except smtplib.SMTPConnectError,e:
    print 'Error connecting to mail server: ',e
    sys.exit(1)

account = str()
password = str()

while len(account) == 0:
    account = raw_input('Using account: ').strip()
while len(password) == 0:
    if 'idlelib.run' in sys.modules:
        password = raw_input('Using password: ').strip()
    else:
        password = getpass.getpass('Using password: ')
    
try:
    m.login(account,password)
except smtplib.SMTPAuthenticationError, e:
    print 'Authentication error: ',e
    sys.exit(1)

msg  = 'From: %s\r\n' % account
msg += 'To: %s\r\n' % to
msg += 'Subject: Date and time fetched from server\r\n\r\n'
msg += 'Current date and time is: %s' % ctime(r.tx_time)

try:
    m.sendmail(account,to,msg)
except Exception,e:
    print 'Error transmitting message: ',e
    sys.exit(1)
    
print 'Message was trasnmitted succesfully to: ',to

m.quit()
