
# printing nth fibonachi number

def n_fibonachii(n: int):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return n_fibonachii(n-1)+n_fibonachii(n-2)


print(n_fibonachii(4))
