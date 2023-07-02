class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left


solution = Solution()
citations = [3, 0, 6, 1, 5]
result = solution.hIndex(citations)
print(result)  # Output: 3
