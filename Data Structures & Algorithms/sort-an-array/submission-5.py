class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr) <=1:
                return arr
            
            mid = len(arr)//2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            left_arr = mergesort(left_arr)
            right_arr = mergesort(right_arr)

            i = 0
            j = 0
            k = 0

            while i < len(left_arr) and j < len(right_arr):
                if (left_arr[i] < right_arr[j]):
                    arr[k] = left_arr[i]
                    k+=1
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    k+=1
                    j+=1
            while i < len(left_arr):
                arr[k] = left_arr[i]
                k+=1
                i+=1
            while j < len(right_arr):
                arr[k] = right_arr[j]
                k+=1
                j+=1
            return arr
        return mergesort(nums)