# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        current_node = self.root
        for item in path_list:
            if item not in current_node.children:
                current_node.insert(item, None)
            current_node = current_node.children[item]

        current_node.handler = handler



    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root

        for item in path_list:
            if not item in current_node.children:
                return None
            current_node = current_node.children[item]

        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, key_path, handler):
        # Insert the node as before
        self.children[key_path] = RouteTrieNode(handler)


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_trie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler


    def add_handler(self, path_string, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        current_trie = self.root_trie
        current_trie.insert(self.split_path(path_string), handler)


    def lookup(self, path_string):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if path_string in ("/", ""):
            return self.root_handler

        current_trie = self.root_trie

        result = current_trie.find(self.split_path(path_string))

        if result is None:
            result = self.not_found_handler

        return result 


    def split_path(self, path_string):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path_string[0] == '/':
            path_string = path_string[1:]
        if path_string[-1] == '/':
            path_string = path_string[:-1]
        
        return path_string.split("/")


# tests

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

if router.lookup("/") == "root handler":
    print('Pass!')
else:
    print('Fail') 

if router.lookup("/home") == "not found handler":
    print('Pass!')
else:
    print('Fail') 
if router.lookup("/home/about") == "about handler":
    print('Pass!')
else:
    print('Fail') 

if router.lookup("/home/about/") == "about handler":
    print('Pass!')
else:
    print('Fail') 
if router.lookup("/home/about/me") == "not found handler":
    print('Pass!')
else:
    print('Fail') 


router = Router("root handler", "Error 404: Not Found") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/path1", "path1 handler")  # add a route
router.add_handler("/home/path1/path12", "path12 handler")  # add a route
router.add_handler("/home/path2/path21/path22", "path22 handler")  # add a route
router.add_handler("/home/path3/path31", "path31 handler")  # add a route

if router.lookup("/home/path1") == "path1 handler":
    print('Pass!')
else:
    print('Fail') 

if router.lookup("/home/path1/path12") == "path12 handler":
    print('Pass!')
else:
    print('Fail') 

if router.lookup("/home/path2/path21/path22") == "path22 handler":
    print('Pass!')
else:
    print('Fail') 

if router.lookup("/home/path3/path31/") == "path31 handler":
    print('Pass!')
else:
    print('Fail') 

if router.lookup("/home/path1/noexist") == "Error 404: Not Found":
    print('Pass!')
else:
    print('Fail') 
