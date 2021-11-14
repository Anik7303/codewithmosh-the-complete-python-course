from timeit import timeit

# try:
#     x = int(input('Age: '))
# except SyntaxError as error:
#     print(error)
# except (ValueError, ZeroDivisionError):
#     pass
# else:
#     pass
# finally:
#     print('Execution complete')

code1 = """
def calculate_xfactor(age):
    if(age > 0):
        return 10 / age
    raise ValueError("Age cannot be 0 or less")

try:
    calculate_xfactor(-1)
except (ValueError, ZeroDivisionError):
    pass
"""

code2 = """
def calculate_xfactor(age):
    return 10 / age if age > 0 else None

xfactor = calculate_xfactor(-1)
if xfactor is None:
    pass
"""

print(
    f'first: {timeit(code1, number=10000)} | second: {timeit(code2, number=10000)}')

# try:
#     file = open('exceptions.py', encoding='utf-8')
#     print('file opened')
# except Exception:
#     pass
# else:
#     pass
# finally:
#     file.close()


# try:
#     # with will autometically close the file
#     # after the block of code has been executed
#     # with works with classes that have __enter__() and __exit__()
#     with open('exceptions.py') as file:
#         pass
# except Exception:
#     pass
