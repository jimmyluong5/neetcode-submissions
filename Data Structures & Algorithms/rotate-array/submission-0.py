class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        #you can take i+k and mod it by the length of the len(nums) because mod tells you how deep you are into an array

        #then copy the elements into an array that is O(n) space and O(n) time

        #another method to do it in place would be swap the last k elements and the n-k elements 

        #so you first reverse the array then take the first k elements and revesre that and the last k elements and reverse that
        n = len(nums)
        k = k%n


        #this function will just reverse the array and output array
        def helper(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1
            return arr
        
        #so we need to do this
        #1. reverse the original nums array
        #2. reverse the first k elements from left to k-1
        #3 reverse the remaining elements which is n-k so from k+1 to right
        #call the helper function
        arr = helper(nums, 0, n-1)

        #then you reverse the first k elements from left to k-1
        arr = helper(arr, 0, k-1)

        #then you reverse the n-k elements which is from k to n-1
        arr = helper(arr, k, n-1)

        return arr