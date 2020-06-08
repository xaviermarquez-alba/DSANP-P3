# Dutch National Flag Problem
## Data Structure & Time/Space complexity

For this problem we need to sort the array in one traverse, the approach used was, first we start with an empty list and append the 2's to the right, 0's to the start, and keep the mid index to add the 1's next to the last 1 added.

The time complexity is O(n) (we visit the entire array), and the space complexity is O(n) for the input array + 0(n) for the result list
