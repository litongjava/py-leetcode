class Solution(object):
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True

solution = Solution()
nums = [2, 3, 1, 1, 4]
result = solution.canJump(nums)
print(result)  # Output: True
