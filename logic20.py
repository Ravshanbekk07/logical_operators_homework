def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.

    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    count_0 = 0
    count_1 = 0

    x1 = n % 10
    x2 = n % 10
    x3 = n//100 % 2
    x4 = n//100 % 2
    x5 = n//100/100

    if x1 == 1:
        count_1 += 1
    else:
        count_0 += 1

    if x2 == 1:
        count_1 += 1
    else:
        count_0 += 1

    if x3 == 1:
        count_1 += 1
    else:
        count_0 += 1

    if x4 == 1:
        count_1 += 1
    else:
        count_0 += 1

    if x5 == 1:
        count_1 += 1
    else:
        count_0 += 1

    return count_1 > count_0


# v = main(1100)
v = main(10011)
print(v)
