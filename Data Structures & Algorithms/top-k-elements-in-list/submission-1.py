class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)): # Efficiency n
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1

        # Now map = {1: count, 2: count, etc.
        solution = []
        counts = []
        orderedCounts = list(sorted(map.values())) # Efficiency n*log(n)
        for i in range(k): # Efficiency (n)
            counts.append(orderedCounts[-i - 1])
        for j in map: # Efficiency (n)
            if map[j] in counts:
                solution.append(j)
        return solution # Efficiency n^3 * log(n) + n