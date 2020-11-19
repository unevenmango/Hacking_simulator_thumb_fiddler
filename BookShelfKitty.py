def checkuser(user,f):
    Users = f.readlines()
    if user in Users:
        return 0
    
    f.writelines(Users + [user])
    return 1

def adduser(f):
    username = raw_input("Username")
    b = checkuser(username,f)
    if b:
        print("[!UsernameCreated!]")
    else:
        print("username already exsists")

try:
    with open("users.txt") as f:
        Users = f.readlines()
        if len(Users) == 1:
            print("First User Detected")
            adduser(f)

except IOError:
    f = open("users.txt","w")
    f.write("Hiiii I store The Users!  :)")
    f.close()
    print("Initializing")


