import random


class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val):
        if val in self.index_map:
            return False
        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        if val not in self.index_map:
            return False
        idx = self.index_map[val]
        last_val = self.nums[-1]
        self.nums[idx] = last_val
        self.index_map[last_val] = idx
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        rand_idx = random.randint(0, len(self.nums) - 1)
        return self.nums[rand_idx]


randomizedSet = RandomizedSet()
randomizedSet.insert(1)  # Returns True
randomizedSet.remove(2)  # Returns False
randomizedSet.insert(2)  # Returns True
randomizedSet.getRandom()  # Returns either 1 or 2 randomly
randomizedSet.remove(1)  # Returns True
randomizedSet.insert(2)  # Returns False
randomizedSet.getRandom()  # Returns 2
