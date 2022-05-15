class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) <= 1: return False
        dict = {}

        left = 0
        right = len(nums) - 1

        while (left <= right):
            if dict.get(nums[left]) is not None:
                return True
            else:
                dict[nums[left]] = left
            left += 1

            if dict.get(nums[right]) is not None:
                return True
            else:
                dict[nums[right]] = right
            right -= 1

            if left == right:
                if dict.get(nums[left]) is not None:
                    return True
                else:
                    return False

        return False

if __name__ == '__main__':
    l = Solution()
    # print(l.longestPalindrome('aacabdkacaa'))
    print(l.containsDuplicate([1000000000,1000000000,11]))

