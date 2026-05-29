class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = {}
        for i in nums: 
            if(i not in arr):
                arr[i] = 0
            arr[i] += 1
        arr = sorted(arr.items(), key = lambda x: x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(arr[i][0])
        return result
            
            
