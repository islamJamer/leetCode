
class Solution:

    def maxArea1(self, height: list[int]) -> int:
        # O(n^2)

        if len(height) <= 1: return 0
        if len(height) == 2: return min(height[0], height[1])

        max_area = 0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r-l) * min(height[l], height[r])
                max_area = max(max_area, area)
        return max_area

    def maxArea2(self, height: list[int]) -> int:
        # O(n^2)

        if len(height) <= 1: return 0
        if len(height) == 2: return min(height[0], height[1])

        r = len(height) - 1
        max_area = 0
        l = 0
        while (r > l):
            if r < len(height) - 1 and height[r] == height[r + 1]: continue
            while (l < r):
                if l != 0 and height[l - 1] == height[l]: continue
                min_height = min(height[l], height[r])
                loc_max_area = min_height * len(height[l:r])
                max_area = max(max_area, loc_max_area)
                l += 1
            l = 0
            r -= 1
        return max_area

    def maxArea(self, height: list[int]) -> int:
        if len(height) <= 1: return 0
        l,r = 0, len(height)-1
        max_area = 0
        while(l < r):
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[r] > height[l]: l+=1
            else: r -= 1
        return max_area



if __name__ == '__main__':
    s = Solution()

    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    # print(s.maxArea([2, 3, 4, 5, 18, 17, 6]))

