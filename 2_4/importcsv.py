#!/usr/bin/python
# Nicolae Erast - 02.05.2017

__all__ = []

print 'Demo importing csv and dynamic object creation\n'

def main():
    csv = open('mycsv.csv')

    # define class attributes and the class itself
    cls_attr = {'obj':list(),'max':0}
    db = type('db', (object,), cls_attr)

    # define __init__
    def db__init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v
            if len(v) > db.max:
                db.max = len(v)
        db.obj.append(self)
    db.__init__ = db__init__

    # define __str__
    def db__str__(self):
        rec = []
        for field in fields:
            rec.append(self.__dict__[field])
        return '\t'.join([r.ljust(db.max) for r in rec])
    db.__str__ = db__str__

    # reading records and adding objects
    fields = csv.readline().strip().split(',')
    for line in csv:
        line = line.strip().split(',')
        rec = dict(zip(fields,line))
        db(**rec)

    # printing objects
    print '\t'.join([f.ljust(db.max) for f in fields])
    for r in xrange(0,len(db.obj)):
        print db.obj[r]

    raw_input('\nPress any key to exit')

if __name__ == '__main__':
    main()
else:
    print 'No DRY dude!'
