class Solution:

    def findUnsortedSubarray(self, nums: list[int]) -> int:
        if len(nums) <= 1: return 0
        sorted_nums = sorted(nums)
        if nums == sorted_nums: return 0

        right = 0
        i = 0
        while i< len(nums):
            if nums[i] == sorted_nums[i]:
                i += 1
                continue

            right = i
            i+=1

        left = len(nums)-1
        j = len(nums)-1
        while j >=0:
            if nums[j] == sorted_nums[j]:
                j-=1
                continue

            left = j
            j-=1

        return right - left + 1

if __name__ == '__main__':
    l = Solution()
    print(l.findUnsortedSubarray([1,2,3,4]))