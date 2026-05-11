class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            if target - numbers[i] in seen:
                return [seen[target - numbers[i]] + 1, i + 1]
            else:
                seen[numbers[i]] = i