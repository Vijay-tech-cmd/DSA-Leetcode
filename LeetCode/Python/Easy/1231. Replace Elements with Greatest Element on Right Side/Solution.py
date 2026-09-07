class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = max_value
            if temp > max_value : max_value = temp
        return arr