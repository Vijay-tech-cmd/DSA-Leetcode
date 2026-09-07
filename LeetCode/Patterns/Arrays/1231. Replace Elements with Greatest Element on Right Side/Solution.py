class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        new_l = []
        for i in range(len(arr)-1 , -1, -1):
            curr = arr[i]
            arr[i] = maxi
            maxi = max(curr, maxi)
        return arr