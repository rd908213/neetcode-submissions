class PrefixTree:

    def __init__(self):
        self.trie = TreeNode(None)

    def insert(self, word: str) -> None:
        currentNode = self.trie
        for char in word:
            for child in currentNode.children: # Check children for char
                if child.val == char:
                    currentNode = child
                    break
            else: # If no children found with that char
                newNode = TreeNode(char)
                currentNode.addChild(newNode)
                currentNode = newNode
        currentNode.isLast = True # Add the flag for being a valid end

    def search(self, word: str) -> bool:
        currentNode = self.trie
        for char in word:
            for child in currentNode.children:
                if child.val == char:
                    currentNode = child
                    break
            else:
                return False
        return currentNode.isLast

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.trie
        for char in prefix:
            for child in currentNode.children:
                if child.val == char:
                    currentNode = child
                    break
            else:
                return False
        return True
        

class TreeNode:
    def __init__(self, val: str, isLast=False):
        self.val = val
        self.isLast = isLast
        self.children = []
    def addChild(self, child: TreeNode):
        self.children.append(child)