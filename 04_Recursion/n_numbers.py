
# printing 1 to n numbers using Recursion

def n_numbers(n: int):
    if (n == 0):
        return
    n_numbers(n-1)
    print(n, end=" ")


n_numbers(5)
# n_numbers(4)
