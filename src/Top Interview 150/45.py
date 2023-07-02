class Solution(object):
    def jump(self, nums):
        jumps = 0
        current_jump_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps


solution = Solution()
nums = [2, 3, 1, 1, 4]
result = solution.jump(nums)
print(result)  # Output: 2
