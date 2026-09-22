#!/usr/bin/env python3
print("Enter the first number:")
d1 = int(input())
print("Enter the second number:")
d2 = int(input())
ans = d1 * d2
print(f'{d1} x {d2} = {ans}')
if ans > 0:
	print("The result is positive.")
elif ans < 0:
	print("The result is negative.")
else:
	print("The result is positive and negative.")
