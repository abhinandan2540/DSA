
# finding factorial of a number

def n_factorial(n):
    if (n == 0):
        return 1
    return n*n_factorial(n-1)


print(n_factorial(4))
