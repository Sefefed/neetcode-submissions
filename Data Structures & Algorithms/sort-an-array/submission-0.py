class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        def sort(arr):
            if len(arr) <= 1:
                return arr
            mid = (len(arr)) // 2
            left = sort(arr[:mid])
            right = sort(arr[mid:])   
            return merge(left, right)
        return sort(nums)     



       