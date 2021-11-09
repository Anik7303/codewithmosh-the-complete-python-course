import math

students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"

# String
line_text = '''
HI john
'''
print(line_text)
print(len(course_name))
# print(len(line_text))
print(course_name[:-6])

first_name = 'Anik'
last_name = 'Mohammad'
full_name = f'{first_name} {last_name}'
print(full_name)

# String Functions
course = '  python programming  '
print(course.lower())
print(course.upper())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())
print(course.find('pro'))
print(course.find('Pro'))
print(course.replace('p', 'j'))
print(course.replace('p', 'j', 1))  # replace only once
print('pro' in course)  # expression, if 'pro' is in course variable
print('swift' not in course)

# Numbers
x = 1 + 2j  # a + bi , complex numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 3
x = x + 3
x += 3

print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2), math.floor(2.2))

# Type Conversion
# int(x)
# float(x)
# bool(x)
# str(x)

x = input('x: ')
print(type(x))
y = int(x) + 1
print(y)

# Falsy values
# ""
# 0
# None
