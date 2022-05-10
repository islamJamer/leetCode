class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1: return nums 
        
        even = []
        odd = [] 
        
        for i in nums:
            if i %2 ==0:
                even.append(i)
            else:
                odd.append(i)

        nums = []
        while(len(even) > 0):
            nums.append(even.pop())
        
        while(len(odd) > 0):
            nums.append(odd.pop())
        
        return nums