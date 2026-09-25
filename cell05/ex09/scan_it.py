import sys, re

if len(sys.argv) != 3:
    print("None \n")
else:
    pattern = sys.argv[1]
    text = sys.argv[2]

    found = re.findall(pattern, text, flags = 0)
    if len(found) == 0:
        print("None \n")
    else:
        print(len(found))