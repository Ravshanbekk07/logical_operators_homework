def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    un = a%10
    number = a%100//10
    b = a//10//10
    return   (number + un+b)%2 ==1

    

v = main(335)
print(v)