inp = int(input("Enter a number less than 25\n"))
if inp > 25:
    print("ERROR")
else:
    for i in range(inp,26):
        print(f'Inside the loop, my variable is {i}')