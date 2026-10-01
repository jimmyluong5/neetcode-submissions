class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums)-1
        def quicksort(arr, left, right):
            if left < right: #we need the pivot value
                pi = partition(arr, left, right)

                #quicksort the left and right subarrays of the pivot index
                quicksort(arr, left, pi-1)
                quicksort(arr, pi+1, right)
            return arr


        #partition function
        def partition(arr, left, right):
            #initalize our variables and determine the pivot position
            i = left
            j = right-1
            pivot = arr[right]

            while i < j:
                #just make sure all the elements left of the pivot is less than the pivot value
                while i < right and arr[i] < pivot:
                    i+=1
                while j > left and arr[j] >= pivot:
                    j-=1
                #if i < j, then if our pointers stopped moving then we must have a mismatched value in the array
                if i < j:
                    #just swap the values
                    arr[i], arr[j] = arr[j], arr[i]
                    i+=1
                    j-=1
            if arr[i] > pivot:
                #swap the values
                arr[i], arr[right] = arr[right], arr[i]
            return i #return the pivot index.
            

        return quicksort(nums, 0, len(nums)-1)