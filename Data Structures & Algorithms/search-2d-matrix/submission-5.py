class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        megalist = sum(matrix, [])
        i = len(megalist) // 2
        try:
            if self.RecursiveSrch(i, megalist, target):
                return True
        except IndexError:
            return False

    def RecursiveSrch(self, index, sublist, target):
        if index == 0 and sublist[index] != target:
            index = 1 # Its so dumb it works!
        if sublist[index] > target:
            return self.RecursiveSrch(index // 2, sublist[:index], target)
        elif sublist[index] < target:
            return self.RecursiveSrch(index // 2, sublist[index:], target)
        else:
            return True