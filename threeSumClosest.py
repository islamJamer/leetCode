class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) <= 2: return 0
        nums.sort()
        # print(nums)

        result = nums[0] + nums[1] + nums[len(nums) - 1]

        for i in range(0, len(nums) - 2):
            if i>1 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_result = nums[i] + nums[left] + nums[right]

                if current_result < target: left +=1
                else:  right -=1
                
                if abs(target - current_result) < abs(target - result):
                    result = current_result

        return result