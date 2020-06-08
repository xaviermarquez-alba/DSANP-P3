def calc_sqrt_recursive(start, end, number):
    # get mid
    mid = (start + end) // 2

    # base condition
    if start == mid:
        return mid

    mid_power_two = mid * mid

    # if exact sqrt is found
    if mid_power_two == number:
        return mid

    elif mid_power_two > number:
        result = calc_sqrt_recursive(start, mid, number)
    
    else:
        result = calc_sqrt_recursive(mid, end, number)
    
    return result

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number is None or isinstance(number, str):
        return -1
    if number < 0:
        return -1
        
    result = calc_sqrt_recursive(1, number, number)

    return result

# Tests
print ("Pass!" if (3 == sqrt(9)) else "Fail")
print ("Pass!" if (0 == sqrt(0)) else "Fail")
print ("Pass!" if (4 == sqrt(16)) else "Fail")
print ("Pass!" if (1 == sqrt(1)) else "Fail")
print ("Pass!" if (5 == sqrt(27)) else "Fail")
print ("Pass!" if (188 == sqrt(35455)) else "Fail")
print ("Pass!" if (1 == sqrt(2)) else "Fail")
print ("Pass!" if (12 == sqrt(144)) else "Fail")
print ("Pass!" if (256 == sqrt(65656)) else "Fail")
print ("Pass!" if (3333 == sqrt(11111111)) else "Fail")
print ("Pass!" if (-1 == sqrt("ABC")) else "Fail")
print ("Pass!" if (-1 == sqrt("")) else "Fail")
print ("Pass!" if (-1 == sqrt(None)) else "Fail")
print ("Pass!" if (-1 == sqrt("16")) else "Fail")


