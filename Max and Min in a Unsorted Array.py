import random


def get_min_max(list_intergers):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if  list_intergers is None:
        return (None)
    if len(list_intergers) == 0:
        return (None)
    
    current_max = list_intergers[0]
    current_min = list_intergers[0]
    
    for number in list_intergers:
        if number > current_max:
            current_max = number
        if number < current_min:
            current_min = number

    return (current_min, current_max)

l = [i for i in range(0, 10)]  
random.shuffle(l)
print ("Pass!" if ((0, 9) == get_min_max(l)) else "Fail")


l2 = [i for i in range(-999, 999 + 1)]  
random.shuffle(l2)

print ("Pass!" if ((-999, 999) == get_min_max(l2)) else "Fail")


l3 = [i for i in range(0, 999999 + 1)]
random.shuffle(l3)

print ("Pass!" if ((0, 999999) == get_min_max(l3)) else "Fail")


l4 = [i for i in range(-5448, 48188 + 1)]  
random.shuffle(l4)

print ("Pass!" if ((-5448, 48188) == get_min_max(l4)) else "Fail")


l5 = None  
print ("Pass!" if ((None) == get_min_max(l5)) else "Fail")


l6 = []
print ("Pass!" if ((None) == get_min_max(l6)) else "Fail")
