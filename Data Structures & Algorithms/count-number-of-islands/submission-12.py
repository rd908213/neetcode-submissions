class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island_detector(
            i: int, # The number row we are on
            j: int, # The number column we are on
            seen: set, # The coordinates that have already been seen
            island: set =set() # The current island
            ):
            if (i, j) in island: # If we've already seen this node
                return island, seen
            else:
                island.add((i, j))
            
            if i != 0: # North Logic
                seen.add((i-1, j)) # Even if its not part of an island, add it to seen
                if grid[i-1][j] == "1":
                    island, seen = island_detector(
                        i-1,
                        j, # Previous row, same column
                        seen,
                        island=island
                        )
                
            if j != len(grid[i]) - 1: # East
                seen.add((i, j+1))
                if grid[i][j+1] == "1":
                    island, seen = island_detector(
                        i,
                        j+1, # Same row, next column
                        seen,
                        island=island
                        )

            if i != len(grid) - 1: # South
                seen.add((i+1, j))
                if grid[i+1][j] == "1":
                    island, seen = island_detector(
                        i+1,
                        j, # Next row, same column
                        seen,
                        island=island
                        )
            
            if j != 0:
                seen.add((i, j-1))
                if grid[i][j-1] == "1":
                    island, seen = island_detector(
                        i,
                        j-1, # Same row, next column
                        seen,
                        island=island
                        )
            
            return island, seen

        islands: List[set] = []
        seen: set = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in seen and grid[i][j] == "1":
                    island, seen = island_detector(i, j, seen)
                    islands.append(island)
        return(len(islands))
