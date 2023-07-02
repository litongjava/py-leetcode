class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_tank = 0
        curr_tank = 0
        start_idx = 0

        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start_idx = i + 1
                curr_tank = 0

        if total_tank < 0:
            return -1
        else:
            return start_idx

solution = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
result = solution.canCompleteCircuit(gas, cost)
print(result)  # Output: 3
