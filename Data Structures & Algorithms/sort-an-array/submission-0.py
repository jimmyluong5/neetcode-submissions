class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        #lets do mergesort
        def MergeSort(arr):
            #base case
            if len(arr)<=1:
                return arr
            else:
                #create middle pointer
                mid = len(arr)//2

                #left and right arr
                left_arr = arr[0:mid]
                right_arr = arr[mid:len(arr)]
            #merge sort on the left and right sub arrays
            left_sorted=MergeSort(left_arr)
            right_sorted=MergeSort(right_arr)

            #then we need to sort the elements 
            i = 0 #left arr index
            j = 0 #right arr index
            k = 0 #merge arr index

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    #then append to the merged array
                    arr[k] = left_arr[i]
                    #move the pointers
                    k+=1
                    i+=1
                else:
                    arr[k] = right_arr[j]
                    k+=1
                    j+=1
        
            #case 1 where we added all the elements in the right array
            #we have to add all the elements in the left array into the merged arr
            while i < len(left_arr):
                arr[k] = left_arr[i]
                k+=1
                i+=1
            
            #case 2 where we added all the elements in the left array
            #so add all the elements in the right array to merged arr
            while j < len(right_arr):
                arr[k] = right_arr[j]
                k+=1
                j+=1

            return arr
        return MergeSort(nums)