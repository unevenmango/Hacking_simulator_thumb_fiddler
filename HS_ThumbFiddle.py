import os

def prompt(prefix):
    command_line = "$"
    print(command_line)
    usr = input(prefix + " ")
    return usr


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
print('program end')
print('end  even further from my phone')
