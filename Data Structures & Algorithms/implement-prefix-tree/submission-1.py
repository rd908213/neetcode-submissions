class PrefixTree:

    def __init__(self):
        self.trie = TreeNode(None)

    def insert(self, word: str) -> None:
        currentNode = self.trie
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                newNode = TreeNode(char)
                currentNode.addChild(newNode)
                currentNode = newNode
        currentNode.isLast = True # Add the flag for being a valid end

    def search(self, word: str) -> bool:
        currentNode = self.trie
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return False
        return currentNode.isLast

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.trie
        for char in prefix:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return False
        return True
        
class TreeNode:
    def __init__(self, val: str, isLast=False):
        self.val = val
        self.isLast = isLast
        self.children = {}
    def addChild(self, child: TreeNode):
        self.children[child.val] = child