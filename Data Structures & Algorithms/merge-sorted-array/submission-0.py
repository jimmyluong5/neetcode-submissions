class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #inputs are nums1 and nums2"
        #outputs are a sorted array from the element of both of them."

        #nums1 is length of m+n, where m is the elements contain the values to be merged, and n is the number of elements in nums2.

        #first case is that if m == 0, then just return nums2, or set the contents inside nums1 to be the content in nums2

        #must be stored in nums1

        
       
       #we need to use three pointers
       #think about going backwards, and comparing the values at m-1 and n-1,
       #which are the last elements respectively in each array
       #if nums1[p1] > nums2[p2], then override the value at nums1[p], 
       #where p3 is at m+n-1, then move all the ptrs for which you copied from backwards.

       #we use a while loop for all 2/3 pointer methods, if p3 is >= 0 then we keep going, because if p3 == 0 or less we hit behind the array
       
       #make the ptrs
        p1 = m-1 #ptr at the last valid element in nums1
        p2 = n-1 #ptr at the last element in nums2
        p = m+n-1 #ptr at the last element in nums1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                #move all ptrs
                p1 -=1
                p -=1
            else:
                #then nums2[p2] is greater
                nums1[p] = nums2[p2]
                #move all the ptrs
                p2 -=1
                p -= 1
        
        #if num1s array section of size m is smaller then nums2, then we must
        #put the remaining elements into nums1 array.
        #we use p 
        while p1 < 0 and p2>=0:
            nums1[p] = nums2[p2]
            p -=1
            p2 -=1
        return nums1
