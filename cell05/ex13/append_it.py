import sys

l = []

for i in range(1, len(sys.argv)):
    if "ism" in sys.argv[i]:
        pass
    else:
        sys.argv[i] += "ism"
        l.append(sys.argv[i])

if len(l) == 0:
    print("None \n")
else:
    print(l)