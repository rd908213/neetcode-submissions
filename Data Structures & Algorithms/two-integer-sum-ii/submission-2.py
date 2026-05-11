class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = {
            "index1": None,
            "index2": None,
            "subtarget": None
        }

        for i in range(len(numbers)):
            if solution["index1"] == None and target - numbers[i] in numbers:
                solution["index1"] = i
                solution["subtarget"] = target - numbers[i]
            elif numbers[i] == solution["subtarget"]:
                solution["index2"] = i
        return [solution["index1"] + 1, solution["index2"] + 1]