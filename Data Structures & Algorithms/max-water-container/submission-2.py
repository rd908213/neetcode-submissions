class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            if area > max_area: # Do this check each time
                max_area = area

            if heights[l] < heights[r]:
                l += 1
            else: # heights[l] > heights[r]
                r -= 1
        return max_area