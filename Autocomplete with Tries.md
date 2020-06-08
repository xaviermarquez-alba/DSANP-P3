# Autocomplete with Tries
## Data Structure & Time/Space complexity

In this problem we implement a "Trie" data structure for the autocomplete functionality, this will find all end suffixes of a given prefix that have a valid word stored

For the time complexity we have:
- Insert: is  O(n)  with n = len of the word
- Find: is O(n) with n = len of the prefix
- Autocomplete: uses get_suffixes function, this is O(n) with n = numbers of children's, sub-children.., of a word

For the space complexity:
- Insert: is O(n) with n = len of number of children's for that word, this will decrease when we have more repeat prefixes for multiple words
- Find: is O(1) we only return the result node
- Autocomplete: uses get_suffixes function, this is O(n) with n = number of valid suffixes for a given word