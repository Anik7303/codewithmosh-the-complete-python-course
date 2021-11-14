
from sys import getsizeof

print([0]*5)
print(list(range(10)))

letters = ['a', 'b', 'c', 'd', 'e']
numbers = list(range(1, 21))

print(letters[0], letters[0:], letters[:], letters[3:], letters[1:4])
print(numbers[::2], numbers[::-1])
print(letters + numbers)

first, second, *others, last = letters
print(first, second, others, last)

for letter in letters:
    print(letter)

for item in enumerate(letters):
    print(item)

for index, letter in enumerate(letters):
    print(f'{index} => {letter}')

# Add
letters.append("f")  # add to the end of the list
print(letters)
letters.insert(0, '-')  # add to specific index
print(letters)

# Remove
letters.pop()  # remove from the last index
print(letters)
letters.pop(0)  # remove from the specified index
print(letters)
letters.remove('c')  # remove the first occurance of a specified item
print(letters)
del letters[0]  # another way to remove an item from list
print(letters)
del letters[:2]  # remove a range of items
print(letters)
letters.clear()  # clear the list

letters = ['a', 'b', 'c', 'd', 'c', 'e', 'c']

# Find
print(letters.index('e'))  # find the index of an item
print(letters.count('c'))  # count number of occurances
# preventing the occurance of an error in case the item does not exist in the list
if 'c' in letters:
    print(letters.index('c'))

# List Comprehension
print([x * 2 for x in range(5)])  # List
print({x * 2 for x in range(1, 6)})  # Set
print({x: x ** 2 for x in range(1, 10)})  # Dictionary

# Generator Object, reduces memory usage
values = [x * 2 for x in range(1000)]  # using list
# print(values)
# print(f'list: {getsizeof(values)} -> length: {len(values)}')
values = (x * 2 for x in range(10000))  # using generator object
# print(values)
# print(f'gen: {getsizeof(values)}')

# unpacking
numbers = [1, 2, 3, 5]
print(*numbers)
print(*range(10))
print(*"hello world")
first = [1, 3]
second = [2, 4]
print([*first, 5, *second])
first = {'x': 1}
second = {'x': 10, 'y': 3}
print({**first, **second, 'z': 20})
