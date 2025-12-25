
def while_analysis(n: int):
    i = 0
    while i < n:
        print(i)
        i += 2


while_analysis(10)

"""
what's happening here is
------------------------------------------------
a loop running n times with a constat and a constant also adding 

so in general : c1*n+c2 : O(n)
"""
