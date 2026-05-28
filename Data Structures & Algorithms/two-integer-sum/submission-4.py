class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(len(nums)):
            j = i + 1
            arr = []
            for j in range(i + 1,len(nums)):
                if(nums[i] + nums[j] ==  target):
                    arr.append(i)
                    arr.append(j)
                    return arr
            