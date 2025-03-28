from functools import reduce

numbers = [3,5,6,10]

# Using reduce and lambda to calculate the product
product = reduce(lambda a, b: a * b, numbers)

print("Product of 3,5,6 and 10 is:",product)