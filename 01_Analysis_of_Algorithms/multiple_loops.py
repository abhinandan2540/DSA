
# sometimes, we may have multiple loops inside the program running simultaniously.
# that time, calculating 'order of growth' complex but simple to calculate


def mutiple_while_loops(n: int):
    # addition
    # order of growth : O(n)
    i = 0
    while (i < n):
        print(i)
        i += 2
    # multiplication
    # order of growth : O(logn)
    j = 2
    while (j < n):
        print(j)
        j *= 2
    # constant addition
    # order of growth : O(1)
    k = 1
    while (k < n):
        print(k)
        k += 1


mutiple_while_loops(10)

# if we compare, every order of growth
# O(n)+O(logn)+O(1)
# then O(n): will be the total order of growth for the whole code
