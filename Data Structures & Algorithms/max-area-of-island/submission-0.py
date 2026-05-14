class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, seen: set, area: int=0):
            # Immediately return if we've visited this square
            if (i, j) in seen:
                return seen, area
            else:
                seen.add((i, j))
                area += 1
            
            # Perform dfs
            if i != 0 and grid[i-1][j] == 1: # North
                seen, area = dfs(i-1, j, seen, area=area)
            if j != len(grid[i])-1 and grid[i][j+1] == 1: # East
                seen, area = dfs(i, j+1, seen, area=area)
            if i != len(grid)-1 and grid[i+1][j] == 1: # South
                seen, area = dfs(i+1, j, seen, area=area)
            if j != 0 and grid[i][j-1] == 1: # West
                seen, area = dfs(i, j-1, seen, area=area)
            return seen, area
    
        seen = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print((i, j))
                if (i,j) not in seen and grid[i][j] == 1:
                    seen, currArea = dfs(i,j,seen)
                    maxArea = max(maxArea, currArea)
                    print(f"currArea: {currArea}")

        return maxArea