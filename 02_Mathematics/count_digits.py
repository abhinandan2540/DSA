
def count_digits(n: int):
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count


print(count_digits(9275))
print(count_digits(4566325896))
print(count_digits(7))
