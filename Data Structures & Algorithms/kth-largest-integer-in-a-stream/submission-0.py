class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.og_fix_heap(int((len(nums) - 1) / 2))
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        print(f"JUST ADDED {val}")
        self.nums = self.bwd_fix_heap(self.nums)
        print(f"nums: {self.nums}")

        temp_nums = self.nums.copy()
        for i in range(self.k):
            kVal, temp_nums = self.pop(temp_nums)
            print(f"kVal: {kVal}, temp_nums: {temp_nums}")
        return kVal

    def pop(self, nums) -> int:
        res = nums[0]
        nums[0] = nums[-1] # Move the first element to the top of the tree
        nums = self.fwd_fix_heap(nums[:-1])
        return res, nums

    def fwd_fix_heap(self, nums: List[int]):
        parent = 0
        while parent < len(nums):
            lchild = 2 * parent + 1
            rchild = 2 * parent + 2
            # Determine child to use
            if lchild < len(nums) and rchild < len(nums):
                if nums[lchild] > nums[rchild]:
                    child = lchild
                else:
                    child = rchild
            else:
                if lchild < len(nums):
                    child = lchild
                elif rchild < len(nums):
                    child = rchild
                else:
                    return nums
            
            # Check child
            if nums[child] > nums[parent]:
                # Switch right and parent
                newParentValue = nums[child]
                newChildValue = nums[parent]
                nums[parent] = newParentValue
                nums[child] = newChildValue
                parent = child # move parent index
            else:
                return nums
        return nums

    def bwd_fix_heap(self, nums: List[int]):
        child = len(nums) - 1
        while child > 0:
            parent = int((child - 1) / 2)
            if nums[child] > nums[parent]:
                newParentValue = nums[child]
                newChildValue = nums[parent]
                nums[parent] = newParentValue
                nums[child] = newChildValue
                child = parent
            else:
                return nums # Return if the tree is valid to avoid inf loop
        return nums

    def og_fix_heap(self, node=0):
        while node >= 0:
            rchild = 2 * node + 1
            lchild = 2 * node + 2
            if rchild < len(self.nums) and self.nums[rchild] > self.nums[node]:
                newNodeVal = self.nums[rchild]
                newChildVal = self.nums[node]
                self.nums[node] = newNodeVal
                self.nums[rchild] = newChildVal
                self.og_fix_heap(node=rchild)
    
            if lchild < len(self.nums) and self.nums[lchild] > self.nums[node]:
                print(node)
                print(self.nums)
                newNodeVal = self.nums[lchild]
                newChildVal = self.nums[node]
                self.nums[node] = newNodeVal
                self.nums[lchild] = newChildVal
                self.og_fix_heap(node=lchild)
            else:
                node -= 1
        