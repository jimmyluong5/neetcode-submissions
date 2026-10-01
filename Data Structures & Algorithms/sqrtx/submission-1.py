class Solution:
    def mySqrt(self, x: int) -> int:
        #since we know that we can probably brute force to find the sqrt of x, by doing for i in range(x) whatever x is then do i * i = ? then eventually we find a number equal to x, but we can use binary search instead

        #binary search, just do mid * mid < x, if true then move right = mid-1
        #with left = 0 and right = x
        left = 0
        right = x

        while left <= right:
            #mid ptr
            mid = left + (right-left)//2
            if mid * mid < x:
                #the number is on the right side because we need a larger number to reach x
                left = mid+1
            elif mid * mid > x:
                #the number is on the left side, because we need a smaller number to reach x
                right = mid-1
            else:
                return mid
        return right #we use right because in certain cases, left goes past right and if you return that
        #you would be rounding up instead of rounding down.

        
                