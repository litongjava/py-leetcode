class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)

        i = 0
        count = 1

        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                if count < 2:
                    i += 1
                    nums[i] = nums[j]
                    count += 1
            else:
                i += 1
                nums[i] = nums[j]
                count = 1

        return i + 1


solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = solution.removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Output: [1, 1, 2, 2, 3]
