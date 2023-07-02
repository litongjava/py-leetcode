class Solution(object):
    def trap(self, height):
        n = len(height)
        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        water = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = solution.trap(height)
print(result)  # Output: 6
