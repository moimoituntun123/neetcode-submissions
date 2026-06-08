class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i, num in enumerate(nums):
            check = target - num
            if check in arr:
                return([arr[check], i])
            arr[num] = i
        return[] 