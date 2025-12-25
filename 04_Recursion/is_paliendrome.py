
# checking if a string is paliendrome or not
def is_paliendrome(ip: str, start, end):
    """start: starting index 0, 
       end: len(str)-1
    """
    if (start >= end):
        return True
    return (ip[start] == ip[end] and is_paliendrome(ip, start+1, end-1))


print(is_paliendrome('abba', 0, 3))

# time complexity : O(n)
