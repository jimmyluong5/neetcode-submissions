class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        #must return nums1
        #modify nums1 in place

        #since we just add elements from each array and we sort, we start from the smallest element of the nums1 array
       
        p1 = m-1
        p2 = n-1 #we just do two pointers from the back
        p = (m+n)-1

        #we compare the largest element in the arrays then whoever got the largest then we move it at the end of num1s
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                #then we move this value to the end of the array, basically sorting
                nums1[p] = nums1[p1]
                p-=1
                p1-=1
            else: 
                nums1[p] = nums2[p2]
                p-=1
                p2-=1

        #one edge case is that the nums1 valid size is actually smaller, in that case, we just append the rest of the nums2 array to the end of nums1
        while p1 < 0 and p2 >= 0:
            nums1[p] = nums2[p2]
            p-=1
            p2-=1
        return nums1
