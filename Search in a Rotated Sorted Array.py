def custom_binary_search_recursive(start_index, end_index, array, number):
    mid_index = (start_index + end_index) // 2

    # base conditions for recursion
    if array[mid_index] == number:
        return mid_index

    if array[start_index] == number:
        return start_index

    if array[end_index] == number:
        return end_index

    # if array silce is sorted change to normal binary search
    if array[start_index] < array[end_index]:
        # if number not found
        if start_index == mid_index:
            return -1

        if array[mid_index] > number:
            return custom_binary_search_recursive(start_index, mid_index, array, number)
        else:
            return custom_binary_search_recursive(mid_index, end_index, array, number) 
    # if number is in the second slice
    elif (array[start_index] < array[mid_index]) and (number < array[start_index]):
        return custom_binary_search_recursive(mid_index, end_index, array, number)

    # number in first slice
    else:       
        return custom_binary_search_recursive(start_index, mid_index + 1, array, number)



def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    #check valid inputs
    if input_list is None or number is None:
        return -1
    if len(input_list) == 0 :
        return -1
    
    result_index = custom_binary_search_recursive(0, len(input_list) - 1, input_list, number)
    return result_index

def linear_search(input_list, number):
    if input_list is None or number is None:
        return -1
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass!")
    else:
        print("Fail")


# Tests
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5], 10])
test_function([[1], 1])
test_function([[9,1], 1])
test_function([[9,1], 9])
test_function([[], 1])
test_function([None, 1])
test_function([None, None])
test_function([[7,5,6], None])
