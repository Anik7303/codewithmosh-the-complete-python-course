import random
import string

print(random.random())
print(random.randint(1, 2009))
print(random.randrange(1, 2009))
print(random.choice([x for x in range(1, 100, 3)]))

print(random.choices([x for x in range(1, 1000, 7)], k=3))
print(string.ascii_letters, string.digits,
      string.punctuation)
print(random.choices(string.ascii_letters + string.digits, k=10))
pa = random.choices(string.ascii_letters +
                    string.digits + string.punctuation, k=16)
print("".join(pa))

arr = [x for x in range(1, 100)]
print(arr)
random.shuffle(arr)
print(arr)
