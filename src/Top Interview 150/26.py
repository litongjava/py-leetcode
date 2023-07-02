class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

solution = Solution()
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)
print(k)  # Output: 2
print(nums[:k])  # Output: [1, 2]