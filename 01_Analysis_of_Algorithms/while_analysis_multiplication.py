
# now let's analysis an algorithm for multiplication

def while_analysis_multiplication(n: int):
    i = 1
    while i < n:
        print(i)
        i = i*2


# while_analysis_multiplication(10)
while_analysis_multiplication(32)


"""
WHAT'S HAPPENING HERE
-------------------------------------------------
code running k-1 times
c^0 (1), c^1, c^2, c^3...... c^k-1<n
so, order of growth : log(n)

"""
