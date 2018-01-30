#!/usr/bin/python
# Nicolae Erast, 20.04.2017

class util(object):
    lista = []
    def __init__(self):
        util.lista.append(self)

class izatori(object):
    def __init__(self,user,passw):
        self.user = user
        self.passw = passw

class utilizatori(util,izatori):
    def __init__(self,user,passw):
        super(util,self).__init__(user,passw)
        super(utilizatori,self).__init__()

    @staticmethod
    def __useri():
        result = set()
        for u in utilizatori.lista:
            result.add(u.user)
        return result

    # using @classmethod for demo
    @classmethod
    def __parole(cls):
        result = set()
        for p in cls.lista:
            result.add(p.passw)
        return result

class Eroare(Exception):
    def __init__(self,msg):
        super(Eroare,self).__init__(msg) 

def main():
    print 'Demo multiple class inheritance\n'
    
    # cerinta 1 - definire 3 obiecte si tiparire lista user si parola
    user1 = utilizatori('root','4qtsDA5GS*4y')
    user2 = utilizatori('user1','5jAT8Jb@Rp2p')
    user3 = utilizatori('user2','5k4@PgU1lFrJ')

    print 'Set users:'
    print user1._utilizatori__useri()
    print '\nSet passwords:'
    print user3._utilizatori__parole()

    # demo bonus - print a message if len() is used
    try:
        print '\nPrint instance of class utilizatori()'
        print len(user2)
    except (TypeError),e:
        raise Eroare('Object don\'t have this method defined')
            
    raw_input("\nPress any key to exit!")

if __name__ == "__main__":
    main()