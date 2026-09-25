import sys

if len(sys.argv) != 2:
    print("None \n")
else:
    password = sys.argv[1]
    inp = input("What was the parameter? ")
    if password == inp:
        print("Good job!")
    else:
        print("Nope, sorry...")