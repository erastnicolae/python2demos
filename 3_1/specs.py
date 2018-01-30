#!/usr/bin/python
# Nicolae Erast - 07.05.2017

import sys, os, re

def getSpec(exp, f):
    for line in f:
        found = re.match(exp, line)
        if found:
            return ' '.join(found.groups())
    return 'no info found'

def frmtSpecExp(spec):
    output_ex = '((?:\d*[.|,])*\d+)\s*(\S*)'
    return re.escape(spec) + '\s*' +  output_ex

def main():
    print '''
Demo popen and re for win/*nix
    '''
    
    specs = []
    
    if os.name in ['posix']:
        cmd = 'cat /proc/meminfo;'
        specs.append('MemTotal:')
        cmd += 'echo "Network Card(s):" `ls /sys/class/net | grep -v lo | wc -l` "NIC(s)"'
        specs.append('Network Card(s):')

    elif os.name in ['nt']:
        cmd = 'systeminfo'
        specs.append('Total Physical Memory:')
        specs.append('Network Card(s):')
        print specs

    elif True:
        print 'Platform', sys.platform, 'not supported'
        sys.exit(1)

    with os.popen(cmd,'r') as f:
        f = f.readlines()
    
    for spec in specs:
        exp = frmtSpecExp(spec)
        result = getSpec(exp, f)
        print spec, result

    raw_input('\nPress any key to exit!')
    sys.exit(0)
    
if __name__ == '__main__':
    main()
