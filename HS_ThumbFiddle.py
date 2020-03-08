import os
import sys
import random


def NameGen():
    sname = ['DitcherQuick&HydeDivorceLawyers.co', 'Gloooble.com', 'HeevinDistress.com']
    sname1 = ['terse','feint','vain','vituperate','drone','sidestep','repudiate','disingenuous','frugal','pitfall','countenance','sheath','redoubtable','weigh','protracted','overweening','aplomb','delineate','fluke','bogus','palliate','aver','enzyme','catalyst','coagulation','connotation','qualm','embellish','diffidence','shyness','rural','psychotic','madly','bright','fresh','third','adventurous','numberless','extra-large','nonchalant','dull','zesty','adaptable','protective','endurable','poised','illustrious','abrupt','lively','clear','crowded','massive','aberrant','drab','rustic']    
    sname2 = ['past','after','among','save','as','of','in','until','without','beneath','onto','despite','within','following','than','versus','outside','to','above','considering']    
    sname3 = ['.co','.com','.biz','.net']
    ran = random.randint(0,25)    
    if ran > 2:        
        servername = random.choice(sname1) + random.choice(sname2) + random.choice(sname3)    
    else:        
        servername = random.choice(sname)    
    return servername






def ipgen(gate):        
   if gate == 'gate':
       ip1 = random.randint(10, 99) 
       ip2 = random.randint(10, 99) 
       ip3 = random.randint(100, 999)  
       ipgen = str(ip1) + '.' + str(ip2) + '.' + str(ip3) 
   elif gate == 'ran':   
       ip1 = random.randint(100, 400)
       ip2 = random.randint(150, 150)
       ip3 = random.randint(100, 999)
       ip4 = random.randint(10, 150)
       ipgen = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
    else:
       ip1 = random.randint(100, 999)        
       ip2 = random.randint(10, 99)        
       ip3 = random.randint(100, 999)
       ipgen = str(ip1) + '.' + str(ip2) + '.' + str(ip3)
   return ipgen


def prompt(prefix):
    command_line = "$"
    print(command_line)
    usr = input(prefix + " ")
    return usr
if sys.argv[1] == "start":
    user = prompt("username")
    print("your username is " + user)
    cwd = os.getcwd()
    if not os.path.isdir(cwd+'/'+user):
        os.mkdir(user)
        os.chdir(user+'/')
        print(user + ' dosent exsist. creating dir...')
        conf = open(user+'.conf', 'w')
        conf.write(user)
        conf.close
    else:
        print(user + 'already exsists')
    prompt = ""
    while prompt != '-q':
        prompt = prompt(user+'>')
else:
    print(eval(sys.argv[1]))
print('program end')

