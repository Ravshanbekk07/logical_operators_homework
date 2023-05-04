def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    un = a%10
    number = a//10
    return (number + un)%2 ==0

v = main(45)
print(v)