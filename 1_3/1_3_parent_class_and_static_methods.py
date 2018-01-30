#!/usr/bin/python
# Nicolae Erast - 20.04.2017

class coordonate_carteziene(object):
    def __init__(self):
        self.x = coordonate_carteziene.adauga('Hight (x): ')
        self.y = coordonate_carteziene.adauga('Width (y): ')
        self.z = coordonate_carteziene.adauga('Depth (z): ')
    
    @staticmethod
    def adauga(msg):
        while True:
            coord = raw_input(msg)
            try:
                coord = float(coord)
            except(Exception):
                print 'This is not a number'
                continue
            else:
                break
        return coord

class volum(coordonate_carteziene):
    def __init__(self):
        super(volum,self).__init__()
        self.v = self.volum_paralelipiped()
        print "Object volume is: ", self.v

    def volum_paralelipiped(self):
        return self.x * self.y * self.z

    @staticmethod
    def intra_pe_usa(o,u):
        if (o.x < u.l and o.y < u.h) or (o.y < u.l and o.x < u.h):
            return 'The object enter the door using xy axis'
        if (o.x < u.l and o.z < u.h) or  (o.z < u.l and o.x < u.h):
            return 'The object enter the door using xz axis'
        if (o.y < u.l and o.z < u.h) or  (o.z < u.l and o.y < u.h):
            return 'The object enter the door using yz axis'
        return 'Sorry, object is too big to enter the door'

class usa(object):
    def __init__(self):
        self.h = coordonate_carteziene.adauga('Door hight: ')
        self.l = coordonate_carteziene.adauga('Door width: ')
        print 'Door dimensions: ',self.h,'x',self.l

def main():
    print 'Demo class inheritance, parent call and static methods\n'

    # checking maximul volume
    print '# Compute maximum volume #'
    print 'Enter 3 object to compute maximum volume'
    max_volume_obj = 0
    max_volume_units = 0

    for x in xrange(1,4):
        print 'Enter object dimensions',x
        o = volum() # volum instance
        if o.v > max_volume_units:
            max_volume_units = o.v
            max_volume_obj = x
            
    print 'The biggest object volume is',\
        max_volume_obj,'and have', \
        max_volume_units,'units\n'

    # checking if object can be fetched to the door
    print '# Checking if object can enter the door #'
    print 'Enter door\'s dimensions'
    u = usa()
    for x in xrange(1,3):
        print 'Enter object dimensions:'
        o = volum()
        print volum.intra_pe_usa(o,u)
        
    raw_input('\nPress any key to exit!')

if __name__ == '__main__':
    main()
