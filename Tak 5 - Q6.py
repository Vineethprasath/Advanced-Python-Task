# To generate Fibonacci series up to n terms
fibonacci = lambda n: [0, 1] if n == 1 else [0, 1] + [sum([0, 1][i:i+2]) for i in range(1, n-1)]

# Input the number of terms
n = int(input("Enter the number of terms: "))

# Generate Fibonacci series
fib_series = fibonacci(n)

# To print
print(f"Fibonacci series up to {n} terms: {fib_series}")