class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island_detector(
            i: int, # The number row we are on
            j: int, # The number column we are on
            seen: set, # The coordinates that have already been seen
            ):
            if (i, j) in seen: # If we've already seen this node
                return seen
            else:
                seen.add((i, j))
            
            if i != 0: # North Logic
                if grid[i-1][j] == "1":
                    seen = island_detector(
                        i-1,
                        j, # Previous row, same column
                        seen,
                        )
                
            if j != len(grid[i]) - 1: # East
                if grid[i][j+1] == "1":
                    seen = island_detector(
                        i,
                        j+1, # Same row, next column
                        seen,
                        )

            if i != len(grid) - 1: # South
                if grid[i+1][j] == "1":
                    seen = island_detector(
                        i+1,
                        j, # Next row, same column
                        seen,
                        )
            
            if j != 0:
                if grid[i][j-1] == "1":
                    seen = island_detector(
                        i,
                        j-1, # Same row, next column
                        seen,
                        )
            
            return seen

        islandCount = 0
        seen: set = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in seen and grid[i][j] == "1":
                    seen = island_detector(i, j, seen)
                    islandCount += 1
        return(islandCount)
