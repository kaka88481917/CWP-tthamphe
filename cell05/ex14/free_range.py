import sys

if len(sys.argv) != 3:
    print("None \n")
else:
    l = []
    first, second = int(sys.argv[1]), int(sys.argv[2])
    for i in range(first, second + 1):
        l.append(i)
    print(l)