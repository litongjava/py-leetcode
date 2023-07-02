class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)  # Output: 2
print(nums[:k])  # Output: [2, 2]