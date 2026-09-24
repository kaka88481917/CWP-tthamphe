before = [2, 8, 9, 48, 8, 22, -12, 2]
after = []
after_after = []
after_after_after = set()

for num in before:
    after.append(num + 2)

for num in after:
    if num > 5:
        after_after.append(num)

for num in after_after:
    after_after_after.add(num)

print(f"{before}")
print(f"{after_after_after}")