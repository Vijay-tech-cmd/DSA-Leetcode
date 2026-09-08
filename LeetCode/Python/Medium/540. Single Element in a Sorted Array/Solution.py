class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        for num in nums:
            if hashmap[num] == 1:
                return num