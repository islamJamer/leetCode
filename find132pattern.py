class Solution:

    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3: return False

        min_array = [nums[0]] * len(nums)
        stack = []

        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i-1], nums[i])

        j = len(nums)
        for j in range(len(nums)-1, 0, -1):
            if nums[j] > min_array[j]:
                while stack and stack[-1] <= min_array[j]:
                    stack.pop()

                if stack and stack[-1] < nums[j]: return True

                stack.append(nums[j])

        return False

if __name__ == '__main__':
    l = Solution()
    print(l.find132pattern([1,0,0,-4,-3]))
    print('==================================================')
    print(l.find132pattern([1,2,4,5,7,6,8,9,10]))
    print('==================================================')

    print(l.find132pattern([1,2,3,4]))
    print('==================================================')

    print(l.find132pattern([-1,3,2,0]))
    print('==================================================')

    print(l.find132pattern([3,1,4,2]))


