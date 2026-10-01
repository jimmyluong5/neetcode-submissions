class Solution:
    def mySqrt(self, x: int) -> int:
        #also binary search
        #the brute force method consists of asking i*i ==x?

        #but we can do the same thing when binary search
        #if mid * mid > x then our guess is too low, so right = mid-1

        left = 0
        right = x
        while left<=right:
            mid = left + (right-left)//2
            if mid*mid > x:
                right = mid-1
            elif mid*mid < x: 
                left =mid+1
            else:
                return mid
        return right