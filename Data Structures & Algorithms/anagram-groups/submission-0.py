class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = {}
        for i in strs: 
            check = "".join(sorted(i))
            if(check not in arr):
                arr[check] = []
            arr[check].append(i)
        return list(arr.values())

