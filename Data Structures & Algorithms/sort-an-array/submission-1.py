class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #we do merge sort
        def mergesort(arr):
            #first is the base case
            if len(arr) <=1:
                return arr

            else:
                #create middle index
                mid = len(arr)//2

                #create left and right arrays
                left_arr = arr[:mid]
                right_arr = arr[mid:]

            #mergesort on left arr and right arr
            left_sort = mergesort(left_arr)
            right_sort = mergesort(right_arr)

            #then we add each element to the merged arr
            i = 0
            j = 0
            k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    #then we place into arr
                    arr[k] = left_arr[i]
                    k+=1
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    k+=1
                    j+=1
            
            #now if we add all the elements in the left in merge we must add the rest of right_arr
            while j < len(right_arr):
                arr[k] = right_arr[j]
                k+=1
                j+=1

            #same thing with adding all elements in the right
            while i < len(left_arr):
                arr[k] = left_arr[i]
                k+=1
                i+=1
            
            return arr


        return mergesort(nums)