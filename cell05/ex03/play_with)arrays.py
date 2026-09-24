arr = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = [x+2 for x in arr]
arr3 = [x for x in arr2 if x > 5]
sett = set()
for i in arr3:
    sett.add(i)

print(f'{arr}')
print(f'{sett}')