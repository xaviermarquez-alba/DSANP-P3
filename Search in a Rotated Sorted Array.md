# Search in a Rotated Sorted Array
## Data Structure & Time/Space complexity

For this problem I use recursion with a binary search modified, we assume there are no duplicates and the array is rotated once at some point.
The approach uses a modified version of the binary search to slice the array and when the slice is sorted we use normal binary search.

The time complexity is O(log(n)), and the space complexity is O(n) for the input array + O(log(n)) for the call stack.