numbers_list = [0.5, 2, 1, 10, 13.34, 20, 25, 50, 9]

# List comprehension to square even numbers using a lambda
square_of_only_evens = [x**2 for x in numbers_list if (lambda n: n % 2 == 0)(x)]

#Print the given list and square of only evens in the given list
print("Given numbers list:",numbers_list)
print("Square only evens in the given list:",square_of_only_evens)