class Tom_Cruise:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def Do_work(self):
        if self.occupation == 'actor':
            print self.name + " shoots film "
        elif self.occupation == 'tennis player':
            print self.name + " plays tennis"

    def Speaks(self):
        print self.name + " says how are you"


tom = Tom_Cruise("Tom Cruise", "actor")
print "************** Tom Cruise *************************"
tom.Do_work()
tom.Speaks()

maria = Tom_Cruise("Maria Sarapova", "tennis player")
print "************** Maria Sarapova *********************"
maria.Do_work()
maria.Speaks()
