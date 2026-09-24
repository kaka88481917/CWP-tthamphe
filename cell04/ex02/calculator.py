"""Give me the first number: 10
Give me the second number: 2
Thank you!
10 + 2 = 12
10 - 2 = 8
10 / 2 = 5
10 * 2 = 20
"""

a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
print("Thank you!")
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} / {b} = {int(a/b)}')
print(f'{a} * {b} = {a*b}')
