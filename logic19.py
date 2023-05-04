def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    # m = x%10 #3digit number
    # n= x//10//10

    m = x %2 #2digit number
    n = x//10


    return  n ==m

v = main(10)
print(v)

