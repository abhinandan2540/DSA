
# printing n to 1 in recursive way

def printNto1(n: int):
    if (n == 0):
        return
    print(n, end=" ")
    printNto1(n-1)


printNto1(5)
