
# checking if a number is paliendrome or not

def paliendrome_num(n: int):
    return checkNum(n, n, 0)


def checkNum(n, rn, cn):
    if (n == 0):
        if (rn == cn):
            return 1
        else:
            return 0

    cn = cn*10+(n % 10)
    n = n//10
    return checkNum(n, rn, cn)


print(paliendrome_num(101))
