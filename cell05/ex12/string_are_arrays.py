import sys

if len(sys.argv) != 2:
    print("None \n")
else:
    l = []
    for i in sys.argv[1]:
        if i == "z":
            l.append(i)

    if len(l) == 0:
        print("None \n")
    else:
        for i in l:
            print(i, end="")