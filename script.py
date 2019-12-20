'''
import commands
#output = commands.getoutput('ls -l')
output = commands.getoutput('ls')
print output

#num = output.count('polindrome')
num = output.count('elastic')
print num 

'''
'''
import subprocess
subprocess.call("ls",shell = True)  
'''
'''
import subprocess
cmd1 = "echo A listing of the Directory:"
cmd2 = "ls -l"
cmds = [cmd1 , cmd2]
for cmd in cmds:
   subprocess.call(cmd,shell=True)  
'''
