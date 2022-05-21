class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) <= 2:
            return []
        
        nums.sort()
        if nums[0] > 0:
            return []
        
        tuples = []

        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
                
            if nums[i] == nums[i-1] and i >0:
                continue
                
            right = len(nums) - 1
            left = i+1
            while left< right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0: right -=1
                elif sum < 0: left +=1
                else:
                    tuples.append(tuple(sorted([nums[i], nums[left], nums[right]])))

                    left +=1
                    right -=1

        tuples = list(set(tuples))
        # result = list(map(list, tuples))
        return tuples