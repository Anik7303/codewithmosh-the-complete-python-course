from collections import deque
from array import array

# Stack - LIFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(
    f"last {last}, list: {browsing_session}, redirect: {browsing_session[-1]}")
if not browsing_session:
    print('disable')

# Queue - FIFO
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
print(queue.popleft())
print(queue)

# Swap
x = 10
y = 11

x, y = y, x
print(f'x: {x} | y: {y}')

# Array
# Only use if the length of an array is too large and causes performance problems
number = array('i', [1, 2, 3])  # typecodes = 'i', 'I', 'f', 'd', etc
number.append(1)
number.insert(4, 3)
number.pop()
print(number[2])

# Set
numbers = [1, 2, 3, 1, 5, 4, 5]
first = set(numbers)
second = {1, 7, 5}
first.add(11)
first.add(1)
first.remove(3)
print(first)
print(len(first))

print(f'union: {first | second}')
print(f'intersection: {first & second}')
print(f'difference: {first - second}')
print(f'symatric difference: {first ^ second}')

# set does not support indexing
if 11 in first:
    print('yes')
else:
    print('no')

# Dictionaries
point = {"x": 1, "y": 2}
print(point)
point = dict(x=1, y=2, z=3)
print(point, point['x'], point['z'])

print(point.get('a', 0))
del point['x']
print(point)

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)
