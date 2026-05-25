class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seenHash = {}
        def exploreTree(string: str, node: 'TreeNode'):
            isPossible = False
            if (string, node) in seenHash:
                return seenHash[(string, node)]
            if string == "":
                return node.isEnd
            
            char = string[0]

            if char in node.children:
                isPossible = isPossible or exploreTree(string[1:], node.children[string[0]])
            
            if node.isEnd:
                isPossible = isPossible or exploreTree(string, root)

            seenHash[(string, node)] = isPossible

            return isPossible
        
        root = TreeNode()
        for word in wordDict:
            curNode = root
            for char in word:
                if char not in curNode.children:
                    curNode.children[char] = TreeNode(val=char)
                curNode = curNode.children[char]
            curNode.isEnd = True

        return exploreTree(s, root)


class TreeNode:
    def __init__(self, val=None, isEnd=False):
        self.val = val
        self.children = {}
        self.isEnd = isEnd
