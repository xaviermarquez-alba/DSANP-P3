# HTTPRouter using a Trie
## Data Structure & Time/Space complexity

In this problem, we implement an HTTPRouter using a "Trie" data structure, similar to the autocomplete problem, but in his case, we use "parts" of the path as the nodes.

For the time complexity in the worst case we need to check all the nodes, sub-nodes,.. to find the handler for the path.
For the add_handler and lookup function, the time complexity is O(n * m) where n is the number of unique routes  and  m is the length of the longest URL path (separated  by "/")

The space complexity is O(n) with n = numbers of parts for the path.