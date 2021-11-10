
# for loop

for number in range(3):
    print(f'Attempt {number + 1} {(number + 1) * "."}')

for number in range(1, 4):
    print(f'Attempt {number} {number * "."}')

for number in range(1, 10, 2):
    print(f'Attempt {number} {number * "."}')

for x in range(5):
    for y in range(3):
        if x == 3:
            continue
        elif y == 1 and x == 2:
            break
        print(f"({x}, {y})")

for letter in "Program":
    print(letter)

# white loop
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print(command)
