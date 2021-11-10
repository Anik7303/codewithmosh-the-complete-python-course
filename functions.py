def greet(name, title="Mr."):
    print(f"Hello {title} {name}")


def get_greeting(name, title="Mr."):
    return f"Hello {title} {name}"


def increment(number, by=1):
    return number + by


# xargs
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


# xxargs
def save_user(**user):
    print(user)
    for data in user:
        print(f"{data} : {user[data]}")


# greet("Anik")
# print(get_greeting("Anik"))
# print(increment(2))
# print(increment(3, by=2))
# print(multiply(2, 3))
# print(multiply(2, 3, 4, 7))
save_user(id=1, name="John", age=23)
