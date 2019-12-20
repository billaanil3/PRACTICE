import subprocess
import ipaddress
from subprocess import Popen,PIPE
# import pdb
# pdb.set_trace()
network = ipaddress.ip_network('192.168.100.0/24')
print "&&&&&&&&&777777",network.hosts()
for i in network.hosts():
    print "iiiiiiiiiiiiiiiiii",i
    print "ANIIIIIIIIIIIIIIIIII"
    # i = str(i)
    # toping = Popen(['ping','-n','3',i],stdout=PIPE)
    # output = toping.communicate()[0]
    # hostalive = toping.returncode
    # if hostalive == 0:
    #     print i,"is readable"
    # else:
    #     print i,"is unreadabe"
else:
    print "FAAAAAAAAAAA"