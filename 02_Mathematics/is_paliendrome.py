
def is_paliendrome(n: int):
    rev_num = 0
    original = n
    while n > 0:
        ld = n % 10
        rev_num = rev_num*10+ld
        n = n//10
    return rev_num == original

# print(4554 % 10) remainder
# print(4554//10) new num


print(is_paliendrome(4554))
