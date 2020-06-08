## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    
    def get_suffixes(self, prefix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        list_suffixes = []
        
        # base condition, add word to list
        if self.is_word:
            list_suffixes.append(prefix)

        # recursive call to check if the key(char) exist
        childrens_dict = self.children
        for key in childrens_dict:
            current_prefix = prefix + str(key)
            current_node = self.children[key]
            list_suffixes.extend(current_node.get_suffixes(current_prefix))
        
        return list_suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if not char in current_node.children:
                return None    
            current_node = current_node.children[char]

        return current_node

    def autocomplete(self, prefix):
        current_node = self.find(prefix)
        if current_node:
            return current_node.get_suffixes(prefix)
        else:
            return []

 

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Tests

if sorted(MyTrie.autocomplete("ant")) == sorted(['ant', 'anthology', 'antagonist','antonym']):
    print('Pass!')
else:
    print('Fail')


if sorted(MyTrie.autocomplete("fun")) == sorted(['fun', 'function']):
    print('Pass!')
else:
    print('Fail')


if sorted(MyTrie.autocomplete("tri")) == sorted(['trie', 'trigger', 'trigonometry','tripod']):
    print('Pass!')
else:
    print('Fail')


if sorted(MyTrie.autocomplete("a")) == sorted(['ant', 'anthology', 'antagonist','antonym']):
    print('Pass!')
else:
    print('Fail')

if sorted(MyTrie.autocomplete("facto")) == sorted(['factory']):
    print('Pass!')
else:
    print('Fail')

if sorted(MyTrie.autocomplete("apple")) == []:
    print('Pass!')
else:
    print('Fail')

if sorted(MyTrie.autocomplete("")) == sorted(wordList):
    print('Pass!')
else:
    print('Fail')
