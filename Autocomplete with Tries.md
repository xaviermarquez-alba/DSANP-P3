# Autocomplete with Tries
## Data Structure & Time/Space complexity

In this problem I implement a "Trie" data structure for the autocomplete functionality, this will find all end suffixes for a given prefix that corresponds in a valid word

For the time complexity we have:
- Insert: is  O(n)  with n = len of the word
- Find: is O(n) with n = len of the prefix
- Autocomplete: uses get_suffixes function, this is O(n) with n = numbers of children's, sub-children.., of a word

For the space complexity:
- Insert: is O(n * m) with n = len of the word and m is the average of  Trie nodes encountered down 
- Find: is O(1) we only return the result node
- Autocomplete: uses get_suffixes function, this is O(n) with n = number of valid suffixes for a given word