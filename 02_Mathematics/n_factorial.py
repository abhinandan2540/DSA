

def n_factorial(n: int):
    if (n == 1 or n == 0):
        return 1
    return n*n_factorial(n-1)


print(n_factorial(4))
print(n_factorial(5))
print(n_factorial(0))
