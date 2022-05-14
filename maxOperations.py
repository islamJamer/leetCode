class Solution:

    # Using dict O(n)
    def maxOperations1(self, nums: list[int], k: int) -> int:
        dict = {}
        count = 0
        for i in nums:
            if i >= k: continue

            res = k - i

            if dict.get(res) is not None and dict[res]['value'] == i:
                count += 1
                if dict[res]['count'] > 1: dict[res]['count'] -= 1
                else: dict.pop(res)
                continue

            if dict.get(i) is not None: dict[i]['count'] += 1
            else: dict[i] = {'value': res, 'count': 1}

        return count

    # Using array => O(log(n))
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()

        count = 0
        left = 0
        right = len(nums) - 1

        while(left < right):
            sum = nums[left] + nums[right]

            if  sum== k:
                left +=1
                right -= 1
                count +=1

            elif sum > k: right -=1
            else: left+=1


        return count


if __name__ == '__main__':
    l = Solution()
    print(l.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3))
    # print(l.maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4))
