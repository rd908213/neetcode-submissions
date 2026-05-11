class Solution:
    def trap(self, height: List[int]) -> int:
        self.height = height
        total_water = 0
        l, r = self.filter_data()
        while l < r:
            i = 1
            while l + i < r and height[l] >= height[l + i]:
                i += 1
            cur_height = min(height[l], height[l + i])
            total_water += self.calc_water(cur_height, l, l+i)
            l += i
        return total_water
        
            
    def calc_water(self, cur_height, l, r) -> int:
        tot = 0
        for i in range(l, r):
            if cur_height > self.height[i]:
                tot += cur_height - self.height[i]
        return tot

    def filter_data(self) -> tuple[int, int]:
        l = 0
        r = len(self.height)-1
        while l + 1 < len(self.height) - 1 and self.height[l] < self.height[l+1]:
            l += 1
        while r - 1 >= 0 and self.height[r] < self.height[r-1]:
            r -= 1
        return (l, r)
