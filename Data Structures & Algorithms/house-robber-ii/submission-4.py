class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        rob0Arr = [0] * len(nums)
        no0Arr = [0] * len(nums)

        rob0Arr[0] = nums[0]
        rob0Arr[1] = nums[0]
        no0Arr[1] = nums[1]

        for i in range(2,len(nums)):
            # rob0Arr
            if nums[i] + rob0Arr[i-2] > rob0Arr[i-1] and i < len(nums) - 1:
                rob0Arr[i] = nums[i] + rob0Arr[i-2]
            else:
                rob0Arr[i] = rob0Arr[i-1]
            
            # no0Arr
            if nums[i] + no0Arr[i-2] > no0Arr[i-1]:
                no0Arr[i] = nums[i] + no0Arr[i-2]
            else:
                no0Arr[i] = no0Arr[i-1]
        
        return(max(no0Arr[-1], rob0Arr[-1]))