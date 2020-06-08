def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # check valid input
    if input_list is None or len(input_list) == 0:
        return []

    if len(input_list) == 1:
        return input_list

    # sort list asc using mergsort  
    sort_list = mergesort(input_list)

    first_number = ""
    second_number = ""

    for index in range(len(sort_list) - 1, 0, -2):
        first_number +=  str(sort_list[index])
        second_number += str(sort_list[index - 1])

    # add the last digit for odd lists
    if not len(sort_list) % 2 == 0:
        first_number += str(sort_list[0])


    result_list = [int(first_number), int(second_number)]
    return result_list

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass!")
    else:
        print("Fail")


# Tests Cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1, 1, 1, 1, 1], [111, 111]])
test_function([[9, 5, 1, 2, 8, 7, 9, 9], [9972, 9851]])
test_function([[9],[9]])
test_function([None,[]])
test_function([[],[]])

