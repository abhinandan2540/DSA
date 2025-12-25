
# sum of n natural numbers using recursion

def n_sum(n: int):
    if (n <= 1):
        return 1
    return n+n_sum(n-1)


print(n_sum(5))

# time complexity : O(n)
