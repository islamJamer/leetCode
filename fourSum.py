class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <= 2:
            return []

        nums.sort()
        # print(nums)

        tuples = []

        for i in range(0, len(nums)- 3):
            if i >1 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i+1, len(nums)-2):
                left = j+1
                right = len(nums) - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s == target:
                        tuples.append(tuple(sorted([nums[i], nums[j], nums[left], nums[right]])))

                    if s > target: right -=1
                    else: left+=1

        tuples = list(set(tuples))
        # result = list(map(list, tuples))
        return tuples