class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]] += 1
        for i in range(len(nums)):
            if hashmap[nums[i]] == 1:
                return nums[i]            