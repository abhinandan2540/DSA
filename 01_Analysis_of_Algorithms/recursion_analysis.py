
# analysis of recursion

def func_recursive(n: int):
    if (n == 1):
        print('dsa last')
        return
    else:
        print('dsa')
    return func_recursive(n-1)


# func_recursive(10)

# the time complexity of this recurison function is : O(n)


# exmaple 2
def func_recursion_2(n: int):
    if (n == 1):
        print('dsa end')
        return
    for _ in range(n):
        print('dsa')
    func_recursion_2(n-1)
    func_recursion_2(n-1)


func_recursion_2(5)
# time complexity of this recursive function : O(n^2)


# example 3
