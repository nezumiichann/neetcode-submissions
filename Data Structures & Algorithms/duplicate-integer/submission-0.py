class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsAsSet = set(nums)
        return len(nums) != len(numsAsSet)
