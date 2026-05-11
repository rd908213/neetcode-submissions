class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            j = i
            while j < len(heights):
                area = min(heights[j], heights[i]) * (j - i)
                if area > max_area:
                    max_area = area
                j += 1
        return max_area

