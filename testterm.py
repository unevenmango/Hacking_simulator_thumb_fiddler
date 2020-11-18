



datafile = "test.dat"
c = open(datafile, "w")
c.close
f = open(datafile, "r")
if not f:
    exit("data file failed to init")

notes = {}
data = f.read().split("\n")
f.close
for l in data:
    if "#" in l:
        notes[l.split("#")[0]] = l.split("#")[1]
def main():
    opt = input(">> ")
    print("you typed " + opt)
    
    if opt == "q":
        f.close()
        exit("exited")
    elif opt == "n":
        title = input("Title : ")
        note = input("Note : ")
        if title in notes.keys():
            exit("note already exists")
        else:
            dta = "\n".join(data)
            f = open(datafile, "w")
            f.write(dta + "\n" + title + "#" + note)
            print(title + " added")
            f.close()

    main()

main()
