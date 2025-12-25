
def for_analysis(n: int):
    i = 0
    for i in range(1, n, 2):
        print(i)
        i += 2


for_analysis(10)

"""
same logic also applies here
a loop running 'n' times and a constant also adding into it
so 'order of growth' is : O(n)

"""
