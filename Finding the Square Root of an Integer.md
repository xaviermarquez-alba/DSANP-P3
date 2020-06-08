# Square Root of An Integer
## Data Structure & Time/Space complexity

Due to the time complexity requirement O(log(n)) we need to use the binary search approach.
To find the number that corresponds with the solution we need to calc the mid of the number then if mid^2 is equal to the number return mid, else we need to check if is more o less than the expected result and call the function again with the slice that has the result

The time complexity is O(log(n)) due to the binary search algorithm and for the space complexity we need to be aware of the recursion so the function is called O(log(n)) times, every time we save the result variable in the call stack so the space complexity is O(log(n)) too