import string
from random import *
import pdb
characters = string.ascii_letters + string.punctuation + string.digits
pdb.set_trace()
password = "".join(choice(characters) for x in range(randint(8, 16)))
print "-------------", password
x = 10
print x
                                                                                                                                                                                                                                                                                                                                                                                                                