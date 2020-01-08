class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, x in enumerate(nums):
            if x in memo:
                return [memo[x],i]
            memo[target - x] = i
        return [0,1]
