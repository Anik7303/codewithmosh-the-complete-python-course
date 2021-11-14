# Map function
products = [('product1', 10), ('product2', 9), ('product3', 12)]
prices = list(map(lambda item: item[1], products))
print(prices)

# Filter function
x = filter(lambda item: item[1] > 10, products)
filtered_products = list(x)
print(filtered_products)

# List Comprehension
# syntax: [expression for item in items]
# [expression for item in items]
prices = [product[1] for product in products]
# this is the same as `prices = list(map(lambda item: item[1], products))`
print(prices)

filtered_products = [product for product in products if product[1] >= 10]
# this is the same as `list(filter(lambda item: item[1] >= 10, products))`
print(filtered_products)

# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30, 40]
print(list(zip(list1, list2)))
print(list(zip('abedc', list1, list2)))
