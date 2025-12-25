
# analysis for square

def while_square(n: int):
    i = 2
    c = 2
    while i < n:
        print(i)
        i **= c


while_square(32)

"""
This function has a complexity of : O(loglogn)
"""
