class WordDictionary:

    def __init__(self):
        self.base = TreeNode()

    def addWord(self, word: str) -> None:
        curNode = self.base
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TreeNode(char=char)
            curNode = curNode.children[char]
        curNode.isEnd = True

    def search(self, word: str, curNode=None) -> bool:
        if not curNode:
            curNode = self.base
        for i in range(len(word)):
            char = word[i]
            if char == ".":
                truth = [self.search(word[i+1:], curNode = curNode.children[nextNode]) for nextNode in curNode.children]
                return any(truth)
            elif char not in curNode.children:
                return False
            else:
                curNode = curNode.children[char]
        if not curNode.isEnd:
            return False
        return True
        
class TreeNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.isEnd = False
