

datafile = "test.dat"
c = open(datafile, "w")
c.close

def main():
    opt = input(">> ")
    
    if opt == "q":
        
        exit("exited")
    elif opt == "n":
        Notes()
    main()




def Read(path):
    f = open(path)



def Notes():
    title = input("Title : ")
        
    f = open(datafile, "r")

    if not f:
        exit("data file failed to init")
    notes = {}
    data = f.read().split("\n")
    f.close
    for l in data:
        if "#" in l:
            notes[l.split("#")[0]] = l.split("#")[1]
    if title in notes.keys():
        exit("note already exists")
    
    note = input("Note : ")
    dta = "\n".join(data)
    f = open(datafile, "w")
    f.write(dta + "\n" + title + "#" + note)
    print(title + " added")
    f.close()
main()
