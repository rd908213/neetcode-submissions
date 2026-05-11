class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        l, r = self.filter_data(height)
        print(f"Total bound l, r: {l, r}")
        while l < r:
            i = 1
            while l + i < r and height[l] >= height[l + i]:
                i += 1
            print(f"Inner bound l, l+i: {l, l+i}")
            cur_height = min(height[l], height[l + i])
            total_water += self.calc_water(cur_height, height[l:l+i])
            print(f"Total water in this section: {self.calc_water(cur_height, height[l:l+i])}")
            l += i
        return total_water
        
            
    def calc_water(self, cur_height, height: List[int]) -> int:
        tot = 0
        for i in range(len(height)):
            if cur_height > height[i]:
                tot += cur_height - height[i]
        return tot

    def filter_data(self, height: List[int]) -> tuple[int, int]:
        l = 0
        r = len(height)-1
        while l + 1 < len(height) - 1 and height[l] < height[l+1]:
            l += 1
        while r - 1 >= 0 and height[r] < height[r-1]:
            r -= 1
        return (l, r)
