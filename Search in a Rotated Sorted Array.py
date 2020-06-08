def custom_binary_search_recursive(start_index, end_index, array, number):
    mid_index = (start_index + end_index) // 2

    # base conditions for recursion
    if array[mid_index] == number:
        return mid_index

    if array[start_index] == number:
        return start_index

    if array[end_index] == number:
        return end_index

    #logic variables

    # number less than start and end
    number_less_start_end = number < array[start_index] and number < array[end_index]

    # number less than start, end and greater than mid
    number_greater_mid = number_less_start_end and number > array[mid_index]

    # start and end less than mid
    startend_less_mid = (array[start_index] < array[mid_index]) and (array[end_index] < array[mid_index]) and number_less_start_end

    # start and end greater than mid
    startend_greater_mid = (array[start_index] > array[mid_index]) and (array[end_index] > array[mid_index]) and number_greater_mid

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
    elif (startend_less_mid or startend_greater_mid):
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


# add more tests case from review+
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
test_function([test_list, -60])
test_function([[7,5,6,1,2,3,4], 6])
test_function([[1,2,3,4,5,6,7,8,9,10,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0], -6])
test_function([[1,2,3,4,5,6,7,8,9,10,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0], 0])
test_function([[1,2,3,4,5,6,7,8,9,10,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0], 1])


