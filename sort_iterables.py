# Sort
numbers = [3, 51, 2, 8, 6, 23]
letters = ['a', 'b', 'd', 'c']
letters.sort()
print(letters)
numbers.sort()
print(numbers)
numbers = [3, 51, 2, 8, 6, 23]
numbers.sort(reverse=True)
print(numbers)

numbers = [1, 6, 8, 72, 34, 8, 4, 1, 9]
# returns a new sorted list
print(sorted(numbers))

products = [('product1', 10), ('product2', 9), ('product3', 12)]


def sort_item(item):
    return item[1]


products.sort(key=sort_item)
print(products)

# Lambda function | lambda parameters:expression
products = [('product1', 10), ('product2', 9), ('product3', 12)]
products.sort(key=lambda item: item[1])
print(products)
