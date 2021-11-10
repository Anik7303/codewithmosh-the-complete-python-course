count = 0
for number in range(2, 10, 2):
    print(number)
    count += 1
print(f"We have {count} even numbers")

count = 0
for number in range(1, 10):
    if not number % 2:
        print(number)
        count += 1
    else:
        print('.')
print(f"We have {count} even numbers")
